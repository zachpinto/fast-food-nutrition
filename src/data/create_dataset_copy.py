import pandas as pd

# Path to the original CSV file
original_file_path = ('/Users/pintoza/Desktop/dev/data-science/fast-food-nutrition/data/processed/'
                      'all_restaurants_menu_items.csv')

# Path to the new CSV file
new_file_path = '/Users/pintoza/Desktop/dev/data-science/fast-food-nutrition/data/processed/items.csv'

# Read the original CSV file
df = pd.read_csv(original_file_path)

# Save the DataFrame to the new CSV file
df.to_csv(new_file_path, index=False)

print(f"Copied '{original_file_path}' to '{new_file_path}'")
