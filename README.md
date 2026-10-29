# 📚 BooksToScrape Playwright Collector

A robust, multi-page web scraper built with **Python** and **Playwright** to extract book titles and prices from [books.toscrape.com](https://books.toscrape.com/), clean the data, and export it into a structured CSV file.

## 🚀 Features

- **Automated Pagination:** Automatically detects and navigates through all available catalog pages using dynamic `while` loops and click interactions.
- **Data Cleaning:** Automatically strips currency symbols (e.g., "£") and converts string prices into clean `float` values for analytical use.
- **Structured Export:** Uses Python's built-in `csv` module with `DictWriter` to generate a clean, ready-to-use CSV file (`books_all_pages.csv`).
- **Headless/Headful Flexibility:** Built using Playwright's sync API, allowing you to watch the browser execution or run it in the background.

## 🛠️ Technologies Used

- **Python 3.x**
- **Playwright** (`playwright.sync_api`)
- **CSV Module** (Built-in)

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/BooksToScrape-Playwright-Collector.git](https://github.com/your-username/BooksToScrape-Playwright-Collector.git)
   cd BooksToScrape-Playwright-Collector
