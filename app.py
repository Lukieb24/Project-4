import pandas as pd
import streamlit as st
import plotly.express as px



df = pd.read_csv('vehicles_us.csv')


# Check for duplicates and display the count
st.sidebar.subheader('Duplicate Data Check')
n_duplicates = df.duplicated().sum()
st.sidebar.write(f'Number of duplicate rows: {n_duplicates}')

# Remove duplicates if they exist
if n_duplicates > 0:
    df.drop_duplicates(inplace=True)

# Handle missing data: Add a section to show missing data information
st.sidebar.subheader('Missing Data Check')
missing_data = df.isna().sum().to_frame().reset_index()
missing_data.columns = ['Column', 'Missing Values']
st.sidebar.write(missing_data)

# Fill missing values for the 'cylinders' column by grouping by 'model' and 'model_year' and taking the median
df['cylinders'] = df.groupby(['model', 'model_year'])['cylinders'].transform(lambda x: x.fillna(x.median()))

# Display missing data after filling cylinders
st.sidebar.subheader('Missing Data Check (After filling cylinders)')
missing_data_after = df.isna().sum().to_frame().reset_index()
missing_data_after.columns = ['Column', 'Missing Values']
st.sidebar.write(missing_data_after)

# Add header and introduction to the app
st.header('Vehicle Dataset Analysis')

st.write("""
This dashboard presents an exploratory analysis of the vehicle dataset. We analyze key variables such as price, odometer readings, and the number of cylinders, aiming to identify trends and patterns.
""")

# Add interactivity: Dropdown filter for vehicle condition
condition_filter = st.sidebar.selectbox("Select Vehicle Condition", options=df['condition'].unique(), index=0)
filtered_df = df[df['condition'] == condition_filter]

# Histogram for vehicle prices
st.subheader('Histogram of Vehicle Prices')
st.plotly_chart(px.histogram(filtered_df, x='price', nbins=50, title=f'Price Distribution for Condition: {condition_filter}'))

st.write(f"**Conclusion:** For vehicles in **{condition_filter}** condition, prices show a right-skewed distribution, with most priced under $30,000. Outliers exist at higher price points.")

# Checkbox for displaying the odometer histogram
if st.checkbox('Show Odometer Histogram'):
    st.subheader('Histogram of Odometer Readings')
    st.plotly_chart(px.histogram(filtered_df, x='odometer', nbins=50, title=f'Odometer Distribution for Condition: {condition_filter}'))
    st.write(f"**Conclusion:** Vehicles in **{condition_filter}** condition mostly have odometer readings below 150,000 miles, with a peak near 100,000 miles.")

# Scatter plot for Price vs Odometer
st.subheader('Scatter Plot: Price vs Odometer')
st.plotly_chart(px.scatter(filtered_df, x='odometer', y='price', title=f'Price vs Odometer for Condition: {condition_filter}',
                           labels={'odometer': 'Odometer (miles)', 'price': 'Price (USD)'}))
st.write(f"**Conclusion:** In **{condition_filter}** condition, a negative relationship between odometer readings and price is evident: vehicles with higher mileage tend to have lower prices.")

# Scatter plot for Price vs Cylinders
st.subheader('Scatter Plot: Price vs Cylinders')
st.plotly_chart(px.scatter(filtered_df, x='cylinders', y='price', title=f'Price vs Cylinders for Condition: {condition_filter}',
                           labels={'cylinders': 'Cylinders', 'price': 'Price (USD)'}))
st.write(f"**Conclusion:** In **{condition_filter}** condition, vehicles with more cylinders are generally priced higher, with a noticeable increase in price for those with 8 or more cylinders.")

# New chart: Price Distribution by Manufacturer
st.subheader('Box Plot: Price Distribution by Manufacturer')
st.plotly_chart(px.box(filtered_df, x='manufacturer', y='price', title=f'Price Distribution by Manufacturer for Condition: {condition_filter}',
                       labels={'manufacturer': 'Manufacturer', 'price': 'Price (USD)'}))
st.write(f"**Conclusion:** Prices vary significantly between manufacturers. Premium brands tend to have a higher price range compared to more common brands in **{condition_filter}** condition.")
