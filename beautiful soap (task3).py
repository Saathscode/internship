import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape book titles and prices
def scrape_books(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    books = []
    
    # Example: Scraping book titles and prices
    for book in soup.find_all('div', class_='book'):
        title = book.find('h2').text.strip()
        price = book.find('p', class_='price').text.strip()
        books.append({'Title': title, 'Price': price})
    
    return books

# Function to write data to CSV file
def write_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Title', 'Price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for book in data:
            writer.writerow(book)

if __name__ == '__main__':
    base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
    num_pages = 5  # Number of pages to scrape
    
    all_books = []
    
    for page in range(1, num_pages + 1):
        url = base_url.format(page)
        books = scrape_books(url)
        all_books.extend(books)
    
    # Print first few books to verify
    print("First few books scraped:")
    print(all_books[:5])
    
    # Write data to CSV file
    csv_filename = 'scraped_books.csv'
    write_to_csv(all_books, csv_filename)
    
    print(f"Scraped data written to {csv_filename}")
