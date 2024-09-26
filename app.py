import streamlit as st
import os
import re
import sqlite3
from datetime import datetime
from scraper.scraper import scrape_website
from scraper.markdown import convert_to_markdown
from slack.bot import send_markdown_to_slack

# Helper function to sanitize filenames (remove unsafe characters)
def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name)

# Initialize SQLite connection and create the table if it doesn't exist
def init_db():
    conn = sqlite3.connect("scraper_db.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scrape_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            timestamp TEXT,
            file_path TEXT
        )
    ''')
    conn.commit()
    return conn

# Function to log scrape data into the database
def log_scrape_data(conn, url, file_path):
    cursor = conn.cursor()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('INSERT INTO scrape_history (url, timestamp, file_path) VALUES (?, ?, ?)', (url, timestamp, file_path))
    conn.commit()

# Function to retrieve scrape history from the database
def get_scrape_history(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT id, url, timestamp, file_path FROM scrape_history ORDER BY timestamp DESC')
    return cursor.fetchall()

# Streamlit app
def streamlit_app():
    conn = init_db()
    
    st.title("Website Scraper for Static and Dynamic Content")
    
    # User inputs
    url = st.text_input("Enter the website URL:")
    dynamic = st.checkbox("Is this a dynamic website (JavaScript-heavy)?")
    channel = st.text_input("Enter Slack channel (optional):")
    
    if st.button("Scrape Website"):
        if url:
            with st.spinner("Scraping in progress..."):
                # Scrape the website (grouped by page)
                scraped_content_by_page = scrape_website(url, dynamic=dynamic)

                # Create a filename and directory for this session (based on URL and timestamp)
                filename = f"{sanitize_filename(url.split('//')[-1])}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
                file_path = os.path.join("scraped_results", filename)
                os.makedirs("scraped_results", exist_ok=True)
                
                # Consolidate content into one markdown file
                markdown_content = ""
                for page_url, content in scraped_content_by_page.items():
                    markdown_content += f"# {page_url}\n\n"  # Page-level heading
                    markdown_content += convert_to_markdown(content)  # Convert the content to markdown format
                
                # Save the markdown content to a file
                with open(file_path, "w") as file:
                    file.write(markdown_content)
                
                # Log the scrape event in the database
                log_scrape_data(conn, url, file_path)
                
                st.success(f"Scraping completed! Markdown file saved at {file_path}")
                
                # Provide a download button for the markdown file
                with open(file_path, 'r') as file:
                    st.download_button(f"Download {filename}", file, file_name=filename)

                # Optionally send the file to Slack if the user provides a channel
                if channel:
                    send_markdown_to_slack(channel, file_path)
                    st.success(f"Markdown file sent to Slack channel: {channel}")
        else:
            st.error("Please enter a valid URL.")
    
    # Display previous scrapes
    st.subheader("Previous Scrapes")
    history = get_scrape_history(conn)
    if history:
        for entry in history:
            st.markdown(f"**URL:** {entry[1]} - **Scraped on:** {entry[2]}")
            with open(entry[3], 'r') as file:
                st.download_button(f"Download {entry[1]}.md", file, file_name=entry[1] + ".md")
    else:
        st.write("No previous scrapes found.")
    
    # Close the database connection
    conn.close()

if __name__ == "__main__":
    streamlit_app()
