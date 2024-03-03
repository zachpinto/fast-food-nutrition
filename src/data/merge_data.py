import pandas as pd

items_df = pd.read_csv('/Users/pintoza/Desktop/dev/data-science/fast-food-nutrition/data/processed/items.csv')
classifications_df = pd.read_csv('/Users/pintoza/Desktop/dev/data-science/fast-food-nutrition/data/processed/'
                                 'classifications.csv')

# check if the number of rows in items_df and classifications_df are the same
if items_df.shape[0] != classifications_df.shape[0]:
    raise ValueError("The number of rows in items_df and classifications_df are not the same")

# Append the classifications to the items_df
items_df['Classification'] = classifications_df['Classification']

# Save the updated items_df to a new CSV file
items_df.to_csv('/Users/pintoza/Desktop/dev/data-science/fast-food-nutrition/data/processed/'
                'items_with_class.csv', index=False)