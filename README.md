# WEB-SCRAPPING-
Web Scraping: Largest U.S. Companies by Revenue

This project scrapes data from the Wikipedia page listing the largest companies in the United States by revenue. Using BeautifulSoup and Pandas, the script extracts tabular data, processes it, and saves the results as a CSV file.
Key Steps

    Data Extraction:
        Access the webpage using requests.
        Parse HTML content with BeautifulSoup.
        Locate and extract the desired table data.

    Data Processing:
        Extract headers (<th>) and rows (<tr>).
        Populate a DataFrame with structured data.

    Output:
        Save the extracted data as a CSV file (Companies.csv).

Requirements

    Libraries: requests, BeautifulSoup4, pandas.

Usage

    Run the script to scrape the table.
    Output is saved at C:\Users\DELL\OneDrive\Documents\Companies.csv.

