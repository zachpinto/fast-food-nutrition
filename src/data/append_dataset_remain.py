import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

# Load the .env file to get the API key
load_dotenv()

# Initialize the OpenAI client with your API key
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)

# Load the items CSV file
file_path = '/Users/pintoza/Desktop/dev/data-science/fast-food-nutrition/data/processed/items.csv'
items_df = pd.read_csv(file_path)

# Define the batch size
batch_size = 200

# Specify the row to start from
start_from_row = 17587

# Path for the output classifications file
output_file_path = '/Users/pintoza/Desktop/dev/data-science/fast-food-nutrition/data/processed/classifications.csv'

# Function to classify items and append to classifications.csv
def classify_items(items_batch):
    with open(output_file_path, 'a') as output_file:  # Append mode
        for index, item in items_batch.iterrows():
            messages = [
                {"role": "system",
                 "content": "Classify the following food item as one of the following categories: "
                            "main, side, beverage, dessert, or topping. "
                            "The response must be one of these categories only. "
                            "You absolutely must put something no matter what. If you are truly"
                            "unsure what something is, understand that toppings are typically "
                            "single-ingredient items and usually smaller in calories. "
                            "Also, beverages and desserts should be pretty obvious I'd imagine."
                            "Also, if you're unsure between main and side, err on the side of main,"
                            "but remember that sides are typically single-food items."
                            "By the way, if you ever see something that says for, ie beef for bowl,"
                            "that's a topping. If you see something like bowl of beef, that's a main."
                            "For in this context means it's a topping for something else. "
                            "Hope that helps!"},
                {"role": "user", "content": f"Item: {item['Item']}, Calories: {item['Calories']}"}
            ]

            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=messages
                )
                classification = response.choices[0].message.content.strip()
                output_file.write(f"{classification}\n")  # Append each classification
                print(f"Item: {item['Item']} classified as {classification}")
            except Exception as e:
                print(f"Error classifying {item['Item']}: {str(e)}")
                output_file.write("Error\n")  # Append error in case of an exception

# Process the remaining batches
for i in range(start_from_row, len(items_df), batch_size):
    batch = items_df.iloc[i:i + batch_size]
    classify_items(batch)

print("Classification completed and appended to classifications.csv.")
