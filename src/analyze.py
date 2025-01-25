import pandas as pd
import matplotlib.pyplot as plt

# Load the saved CSV file (the file should be in the 'data' folder)
df = pd.read_csv('data/video_data.csv')

# Display the first few rows of the data
print("First few rows of the dataset:")
print(df.head())  # Shows the first 5 rows of the data

# Check for any missing or NaN values
print("\nChecking for missing values:")
print(df.isnull().sum())  # This will show the number of missing values in each column

# Check the column names and data types
print("\nColumns and data types:")
print(df.dtypes)

# Convert views to numeric (if it's not already) to make it easy for analysis
df['Views'] = pd.to_numeric(df['Views'], errors='coerce')

# Get basic statistics about the data (e.g., mean, median)
print("\nBasic statistics about Views:")
print(df['Views'].describe())

# Plot a bar chart for the views of each video
plt.figure(figsize=(12, 8))
plt.bar(df['Title'], df['Views'], color='blue')
plt.xlabel('Video Title')
plt.ylabel('Views')
plt.title('Views for Each Video')
plt.xticks(rotation=90, ha='right')  # Rotate video titles to avoid overlap
plt.tight_layout()  # Adjust layout to avoid clipping
plt.show()
