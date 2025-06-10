from bs4 import BeautifulSoup
import requests
import csv
import time
from urllib.parse import urljoin

base_url = "http://quotes.toscrape.com"
current_url = base_url

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

all_quotes_data = []

print(f"Starting scraping from {base_url}")

while current_url:
    print(f"scraping page: {current_url}")

    try:
        response = requests.get(current_url, headers= HEADERS, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        quotes_on_page = soup.find_all('div', class_ = 'quote')

        if not quotes_on_page:
            print(f"No Quotes found {current_url}. stopping pagination")
            break

        for quote_div in quotes_on_page:
            text_tag = quote_div.find('span', class_='text')
            author_tag = quote_div.find('small', class_='author')

            quote_text = text_tag.get_text(strip=True) if text_tag else 'N/A'
            author_name = author_tag.get_text(strip=True) if author_tag else 'N/A'

            all_quotes_data.append({'Quote': quote_text, 'Author': author_name})


        print(f"Successfully scraped {len(quotes_on_page)} quotes from this page.")

        
        next_button = soup.find('li', class_='next')
        if next_button and next_button.find('a'):
            next_page_relative_url = next_button.find('a')['href']
            current_url = urljoin(base_url, next_page_relative_url)
            time.sleep(1) 

        else:
            print("No 'Next' button found. End of pagination.")
            current_url = None 

    except requests.exceptions.RequestException as e:
        print(f"Error during request to {current_url}: {e}")
        current_url = None # Stop if there's a request error
    except Exception as e:
        print(f"An unexpected error occurred while processing page {current_url}: {e}")
        current_url = None # Stop on unexpected errors

print(f"\nScraping finished. Total quotes extracted: {len(all_quotes_data)}")

# --- CSV Writing ---
if all_quotes_data:
    csv_filename = "scraped_quotes.csv"
    csv_headers = ['Quote', 'Author'] # Updated headers

    print(f"\nWriting data to {csv_filename}...")

    try:
        with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
            writer.writeheader()
            writer.writerows(all_quotes_data) # Use writerows for a list of dicts

        print(f"Successfully wrote {len(all_quotes_data)} rows to {csv_filename}")
    except IOError as e:
        print(f"I/O error writing to CSV file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while writing CSV: {e}")
else:
    print("\nNo data was scraped, so no CSV file will be generated.")

print("\nProgram finished.")