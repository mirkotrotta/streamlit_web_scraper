# Streamlit Web Scraper

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/github/license/mirkotrotta/streamlit_web_scraper" alt="License">
  <img src="https://img.shields.io/badge/Streamlit-%F0%9F%93%88%20Web%20App-success" alt="Streamlit Web App">
  <img src="https://img.shields.io/badge/Coming%20Soon-Slack%20Integration-orange" alt="Coming Soon">
</p>

## 🌐 A Clean & Simple Web Scraper Built With Streamlit, BeautifulSoup, and Selenium

This **Streamlit Web Scraper** extracts text content from any website, whether it's static or JavaScript-heavy, and saves the data into neatly formatted Markdown files. Ideal for personal research, data collection, or sharing website content with others.

## ✨ Key Features

- **Scrape Dynamic and Static Websites**: Supports JavaScript-rendered content using **Selenium** and traditional HTML scraping using **BeautifulSoup**.
- **Single Markdown File Output**: Consolidates all scraped data into one clean and structured Markdown file, organized by page and section.
- **SQLite-Based Scrape History**: Logs all scraped sessions for future access, allowing you to view or download previous scrapes at any time.
- **Slack Integration (Coming Soon)**: In an upcoming release, scraped data can be sent directly to a Slack channel for easy sharing and collaboration.
- **Cross-Device & Version-Control Friendly**: Built with **Git** in mind, enabling seamless version control and multi-device collaboration.

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

- [Python 3.7+](https://www.python.org/)
- [Git](https://git-scm.com/)
- [Virtualenv](https://virtualenv.pypa.io/) (optional but recommended)

### Installation

1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/mirkotrotta/streamlit_web_scraper.git
   cd streamlit_web_scraper
   ```

2. **Set up a virtual environment** (optional, but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (if required, e.g., for future Slack integration):
   - Create a `.env` file and add any necessary environment variables, such as `SLACK_BOT_TOKEN` (for future integration).

5. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

6. Open your browser and go to `http://localhost:8501` to use the app.

---

## 🛠 How to Use

### Scraping a Website
1. **Enter the URL** of the website you want to scrape.
2. **Select if the website is dynamic** (i.e., JavaScript-heavy) or static.
3. **Click "Scrape Website"**: The scraper will retrieve text-based content from the site, organizing it by page and section into a Markdown file.
4. **Download the Markdown file**: Once the scrape is complete, download the file directly through the interface or access previously saved scrapes.

### Features in Progress
- **Slack Integration**: Soon, you'll be able to send scraped data to a specified Slack channel.
- **More Framework Support**: Future experiments include integrating with additional frameworks and APIs for advanced scraping scenarios.

## 🔄 Roadmap

### Planned Features
- **Slack Integration**: Scrape data and automatically send it to a Slack channel for quick collaboration.
- **API Integration**: Adding support for scraping APIs and handling authentication where required.
- **Advanced Scraping Techniques**: Experimenting with frameworks like Playwright for even better dynamic content handling.

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, feel free to:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Mirkotrotta**  
- [GitHub](https://github.com/mirkotrotta)  
- [Twitter](https://twitter.com/mirkotrotta)

---

## 💬 Contact

For any inquiries, questions, or feedback, feel free to open an issue or contact me.
