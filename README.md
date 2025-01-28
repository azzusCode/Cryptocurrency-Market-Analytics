# Cryptocurrency-Market-Analytics

This repository contains a project for analyzing cryptocurrency market data. The data was scraped from [CoinMarketCap](https://coinmarketcap.com/) using Selenium and Python. After performing exploratory data analysis (EDA) and visualizations, the insights were compiled into a Tableau public dashboard for interactive exploration.

## Overview

The goal of this project was to gain insights into the cryptocurrency market by:

- Scraping live market data from CoinMarketCap using Selenium.
- Performing basic exploratory data analysis (EDA) to uncover trends and patterns.
- Visualizing key metrics like market capitalization, trading volume, and price trends.
- Hosting an interactive dashboard on Tableau Public for easy access and analysis.

### Tableau Dashboard
Explore the interactive dashboard here: [Tableau Public Dashboard](https://public.tableau.com/app/profile/md.abidul.mohaimin/viz/CryptocurrencyMarketAnalytics/CryptocurrencyMarketAnalytics)

---

## How to Run the Project

Follow these steps to set up and run the project locally.

### Prerequisites
Make sure you have the following installed:
- Python 3.7 or above
- pip
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/azzusCode/Cryptocurrency-Market-Analytics
   ```

2. **Set Up a Virtual Environment**
   Create and activate a virtual environment to manage dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Script**
   Start the data scraping process:
   ```bash
   python scraper.py
   ```

5. **Analyze the Data**
   Use the provided Jupyter Notebook or Python scripts to perform EDA and visualizations.

---

## Project Files

- **`scraper.py`**: Python script to scrape cryptocurrency data from CoinMarketCap.
- **`Basic_EDA_&_Visualization_of_Crypto_Data.ipynb`**: Colab Notebook for exploratory data analysis and visualizations.
- **`Data/`**: Folder containing the scraped data.
- **`requirements.txt`**: File listing all the required Python libraries.
- **`README.md`**: Project documentation.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to explore the dashboard and use the code for learning or extending your own projects. Contributions and suggestions are welcome!

