import os
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from urllib.parse import urljoin
from src.constants import CATEGORIES, RAW_DATA_DIR, PROCESSED_DATA_DIR
from src.utils import setup_logging

logger = setup_logging("scraper")

# The domain of the directory, to avoid saving their general contact email
EXCLUDE_EMAILS = ["info@hacettepeteknokent.com.tr", "iletisim@hacettepeteknokent.com.tr"]

def scrape_category(category_name, category_url):
    """Scrapes a given category URL for company details."""
    logger.info(f"Starting to scrape category: {category_name} -> {category_url}")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(category_url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch category {category_name}: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all company detail links
    # Assuming links to companies are like /tr/firma/company-name-id
    company_links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        if '/tr/firma/' in href and not href.endswith('/firma_rehberi'):
            # Some links might be duplicates or navigation
            full_url = urljoin(category_url, href)
            company_name = a.text.strip()
            if company_name and full_url not in [link['url'] for link in company_links]:
                company_links.append({"name": company_name, "url": full_url})

    logger.info(f"Found {len(company_links)} companies in {category_name}.")

    data = []
    
    # regex for emails
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

    for i, company in enumerate(company_links):
        comp_name = company["name"]
        comp_url = company["url"]
        logger.info(f"[{i+1}/{len(company_links)}] Scraping {comp_name} ...")
        
        try:
            time.sleep(1.5) # Polite delay
            comp_resp = requests.get(comp_url, headers=headers, timeout=10)
            comp_resp.raise_for_status()
            
            comp_soup = BeautifulSoup(comp_resp.text, 'html.parser')
            
            # Find emails via regex in text
            emails = set(email_pattern.findall(comp_resp.text))
            
            # Filter out general exclude emails and any potential image extensions ending like .png
            valid_emails = []
            for email in emails:
                email_lower = email.lower()
                if email_lower not in EXCLUDE_EMAILS and not email_lower.endswith(('png', 'jpg', 'jpeg', 'gif', 'svg')):
                    valid_emails.append(email_lower)
            
            # Find websites
            websites = set()
            for a in comp_soup.find_all('a', href=True):
                href = a['href']
                if href.startswith('http') and 'hacettepeteknokent.com.tr' not in href and 'hacettepe.edu.tr' not in href and 'argeportal' not in href:
                    websites.add(href)
                    
            data.append({
                "Company Name": comp_name,
                "Directory URL": comp_url,
                "Website": ", ".join(websites) if websites else "",
                "Email": ", ".join(set(valid_emails)) if valid_emails else ""
            })
            
        except Exception as e:
            logger.error(f"Failed to parse company {comp_name} ({comp_url}): {e}")

    # Save to CSV
    if data:
        df = pd.DataFrame(data)
        
        csv_name = CATEGORIES[category_name]["csv_name"]
        
        # Save raw data (all companies)
        raw_path = os.path.join(RAW_DATA_DIR, csv_name)
        df.to_csv(raw_path, index=False, encoding='utf-8-sig')
        logger.info(f"Saved {len(df)} records to {raw_path}")
        
        # Save processed data (only those with emails)
        processed_df = df[df["Email"] != ""]
        processed_path = os.path.join(PROCESSED_DATA_DIR, csv_name)
        processed_df.to_csv(processed_path, index=False, encoding='utf-8-sig')
        logger.info(f"Saved {len(processed_df)} records WITH EMAILS to {processed_path}")
    else:
        logger.warning(f"No data extracted for {category_name}.")

def run_scraper():
    """Main entry point for the scraper."""
    logger.info("Starting scraper for all categories...")
    for cat_name, cat_data in CATEGORIES.items():
        scrape_category(cat_name, cat_data["url"])
    logger.info("Scraping completed. Please review the CSV files in data/processed/ and move approved ones to data/approved/.")

if __name__ == "__main__":
    run_scraper()
