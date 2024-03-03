import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('../../data/processed/final.csv')

# Filter the dataset for 'main' items
df_main = df[df['Classification'] == 'main']

# Define the function to remove outliers
def remove_outliers(group):
    mean = group['Calories'].mean()
    std = group['Calories'].std()
    return group[(group['Calories'] >= (mean - 3 * std)) & (group['Calories'] <= (mean + 3 * std))]

# Apply the outlier removal function and reset index
df_filtered = df_main.groupby('Restaurant').apply(remove_outliers).reset_index(drop=True)

# Calculate median values for each restaurant and sort
median_calories = df_filtered.groupby('Restaurant')['Calories'].median().sort_values(ascending=False)
sorted_restaurants = median_calories.index.tolist()

# Set the aesthetic style of the plots
sns.set_style('whitegrid')
sns.set_context('talk')

# Create the plot
plt.figure(figsize=(12, 50))
box_plot = sns.boxplot(
    x='Calories',
    y='Restaurant',
    data=df_filtered[df_filtered['Restaurant'].isin(sorted_restaurants)],
    order=sorted_restaurants,
    palette='plasma_r',  # Use a warm to cool color palette
    showfliers=False  # This removes the outlier points
)

# Enhance the plot with additional styling
box_plot.set_title('Calorie Distribution of Main Items by Restaurant', fontsize=20)
box_plot.set_xlabel('Calories', fontsize=15)
box_plot.set_ylabel('Restaurant', fontsize=15)
box_plot.tick_params(axis='both', which='major', labelsize=12)

# Display the plot
plt.tight_layout()
plt.show()
