import polars as pl
import matplotlib.pyplot as plt

# URL of the CSV file
url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/covid-geography/mmsa-icu-beds.csv"

# Read the CSV data into a Polars DataFrame
df = pl.read_csv(url)

# Calculate summary statistics for the "total_at_risk" column
total_at_risk_stats = df['total_at_risk'].describe()

# Print the summary statistics
print(total_at_risk_stats)

# Create a DataFrame with your summary statistics
summary_data = pl.DataFrame({
    'Statistic': ['Mean', 'Median', 'Standard Deviation'],
    'Value': [667188.7, 396081.5, 884786.8]
})

# Create a bar chart
plt.figure(figsize=(8, 6))
plt.bar(summary_data['Statistic'].to_pandas(), summary_data['Value'].to_pandas(), color=['blue', 'green', 'red'])
plt.ylabel('Value')
plt.title('Summary Statistics for "total_at_risk"')
plt.show()
