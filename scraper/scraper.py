from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from urllib.parse import urljoin
import requests
import logging
import time

# Initialize logging
logging.basicConfig(filename='scraper_errors.log', level=logging.ERROR, 
                    format='%(asctime)s %(levelname)s %(message)s')

# Function to initialize Selenium WebDriver with Chrome
def init_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

# Function to fetch static content using requests and BeautifulSoup
def fetch_static_page(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch static content from {url}: {e}")
        return None

# Function to fetch dynamic content using Selenium
def fetch_dynamic_page(url):
    driver = init_driver()
    try:
        driver.get(url)
        time.sleep(3)  # Give time for the JavaScript to load
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        return soup
    except Exception as e:
        logging.error(f"Failed to fetch dynamic content from {url}: {e}")
        return None
    finally:
        driver.quit()

# Function to clean the HTML content by removing unnecessary sections
def clean_html_content(soup):
    # Remove navbar, footer, scripts, styles, etc.
    for element in soup(['nav', 'footer', 'aside', 'script', 'style', 'noscript', 'header', 'form']):
        element.decompose()

    # Optionally remove specific elements based on class or id (you can modify this part based on the target site)
    for element in soup.find_all(class_=["navbar", "footer", "advertisement", "sidebar"]):
        element.decompose()

    return soup

# Function to extract relevant content from the cleaned HTML
def extract_relevant_content(soup):
    content = ""
    
    # Extract headings (h1-h6) and paragraphs (p)
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']):
        text = tag.get_text(separator=" ", strip=True)
        if text:
            if tag.name.startswith('h'):
                content += f"\n## {text}\n"  # Markdown format for section headings
            else:
                content += f"\n{text}\n"
    
    return content

# Main function to scrape website with dynamic and static content, returning content grouped by page
def scrape_website(base_url, max_depth=3, dynamic=False):
    visited_urls = set()  # Track visited URLs to avoid loops
    scraped_content_by_page = {}

    def scrape_page(url, depth):
        if url in visited_urls or depth > max_depth:
            return ""
        visited_urls.add(url)

        # Fetch either dynamic or static content based on input
        soup = fetch_dynamic_page(url) if dynamic else fetch_static_page(url)
        if not soup:
            return ""

        # Clean the soup to remove irrelevant sections
        cleaned_soup = clean_html_content(soup)

        # Extract relevant content (headings and paragraphs)
        page_content = extract_relevant_content(cleaned_soup)
        scraped_content_by_page[url] = page_content  # Store content by URL
        
        # Follow internal links recursively (if depth is allowed)
        if depth < max_depth:
            for link in cleaned_soup.find_all('a', href=True):
                href = link['href']
                full_url = urljoin(base_url, href)
                if base_url in full_url and full_url not in visited_urls:
                    scrape_page(full_url, depth + 1)
    
    scrape_page(base_url, 0)
    return scraped_content_by_page
