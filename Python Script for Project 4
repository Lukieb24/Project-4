import plotly.express as px
import pandas as pd

# Load the dataset from your repository
# If it's in a subfolder, add the path relative to your code
df = pd.read_csv('vehicles_us.csv')

# Check the first few rows to understand the structure of the dataset
print(df.head())
fig1 = px.histogram(df, x='price', nbins=10, title='Distribution of Car Prices')
fig1.show()

# Histogram of Car Mileage
fig2 = px.histogram(df, x='mileage', nbins=10, title='Distribution of Car Mileage')
fig2.show()

# Scatterplot of Price vs Mileage
fig3 = px.scatter(df, x='mileage', y='price', title='Price vs Mileage',
                  labels={'x': 'Mileage (in miles)', 'y': 'Price (in $)'})
fig3.show()

# Scatterplot of Price vs Horsepower
fig4 = px.scatter(df, x='horsepower', y='price', title='Price vs Horsepower',
                  labels={'x': 'Horsepower (HP)', 'y': 'Price (in $)'})
fig4.show()
