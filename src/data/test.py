from bs4 import BeautifulSoup
import pandas as pd
import requests

# The URL you're scraping
url = "https://fastfoodnutrition.org/fast-food-restaurants"

# Include headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Make the request to the URL
response = requests.get(url, headers=headers)

# Ensure the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Initialize an empty list to hold the extracted links
    restaurant_links = []

    # Base URL for constructing the full URL
    base_url = 'https://fastfoodnutrition.org'

    # Find all <a> tags and extract the 'href' attributes
    for link in soup.find_all('a', href=True):
        # Skip links that don't contain the path for restaurant pages
        if "/nutrition-facts" not in link['href']:
            # Construct the full URL by appending the 'href' attribute to the base URL
            full_url = base_url + link['href']
            restaurant_links.append(full_url)

    # Convert the list of links into a pandas DataFrame for easy handling
    df_restaurant_links = pd.DataFrame(list(set(restaurant_links)), columns=['Link'])  # Using set to remove duplicates

    csv_file_path = '../data/interim'
    df_restaurant_links.to_csv(csv_file_path, index=False)

    print(f"Restaurant links saved to {csv_file_path}")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
