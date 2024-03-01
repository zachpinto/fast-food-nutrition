import json
from bs4 import BeautifulSoup
import pandas as pd
import requests

# Read the list of restaurant links from the CSV file
restaurant_links = pd.read_csv('../../data/interim/restaurant_links.csv')

# Initialize an empty DataFrame to store the results from all restaurants
all_menu_items = pd.DataFrame()

# Define headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Iterate over each restaurant URL
for index, row in restaurant_links.iterrows():
    url = row['Link']
    # Validate URL format
    if not url.startswith('http'):
        url = 'https://' + url

    restaurant_name = url.split('/')[-1]  # Extracting the restaurant name from the URL

    try:
        # Fetch the page content with headers
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Skipping {url} due to status code {response.status_code}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the script tag with the JSON content
        script_tag = soup.find('script', type='application/ld+json')

        # Check if the script tag is found and proceed with JSON parsing
        if script_tag:
            try:
                menu_data = json.loads(script_tag.string)
                if 'menu' not in menu_data or 'hasMenuSection' not in menu_data['menu']:
                    print(f"Skipping {url} as it does not contain menu data.")
                    continue

                menu_items = []

                # Extract menu item names and calorie information
                for section in menu_data['menu']['hasMenuSection']:
                    for item in section['hasMenuItem']:
                        item_name = item['name']
                        calories = item['nutrition']['calories'].replace(' calories', '')  # Removing 'calories' text
                        menu_items.append({'Restaurant': restaurant_name, 'Item': item_name, 'Calories': calories})

                # Convert the list to a DataFrame
                df_menu_items = pd.DataFrame(menu_items)

                # Append the results to the all_menu_items DataFrame
                all_menu_items = pd.concat([all_menu_items, df_menu_items], ignore_index=True)
            except json.decoder.JSONDecodeError as e:
                print(f"Skipping {url} due to JSON parsing error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

# Save the consolidated data to a CSV file
all_menu_items.to_csv('../../data/processed/all_restaurants_menu_items.csv', index=False)
