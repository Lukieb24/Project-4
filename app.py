import pandas as pd
import streamlit as st
import pandas as pd
import streamlit as st
import plotly.express as px


df = pd.read_csv('vehicles_us.csv')

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing data (fill cylinders column based on median by model and model_year)
df['cylinders'] = df.groupby(['model', 'model_year'])['cylinders'].transform(lambda x: x.fillna(x.median()))

# App Title
st.header('Vehicle Dataset Analysis')

#
condition_filter = st.sidebar.selectbox("Select Vehicle Condition", options=df['condition'].unique(), index=0)

# Filter the dataframe based on selected condition
filtered_df = df[df['condition'] == condition_filter]
# Filter the dataframe based on selected condition
filtered_df = df[df['condition'] == condition_filter]

# Display the columns in filtered_df to confirm 'model' exists
st.write("Columns in filtered_df:", filtered_df.columns)

# Display the first few rows of filtered_df to check the data
st.write("First few rows of filtered_df:")
st.write(filtered_df.head())

# Box Plot: Price Distribution by Model
st.subheader('Box Plot: Price Distribution by Model')
st.plotly_chart(px.box(filtered_df, x='model', y='price', title=f'Price Distribution by Model for Condition: {condition_filter}'))

# Histogram of vehicle prices
st.subheader('Histogram of Vehicle Prices')
st.plotly_chart(px.histogram(filtered_df, x='price', nbins=50, title=f'Price Distribution for Condition: {condition_filter}'))

# Checkbox to show Odometer histogram
if st.checkbox('Show Odometer Histogram'):
    st.subheader('Histogram of Odometer Readings')
    st.plotly_chart(px.histogram(filtered_df, x='odometer', nbins=50, title=f'Odometer Distribution for Condition: {condition_filter}'))

# Scatter plot for Price vs Odometer
st.subheader('Scatter Plot: Price vs Odometer')
st.plotly_chart(px.scatter(filtered_df, x='odometer', y='price', title=f'Price vs Odometer for Condition: {condition_filter}'))

# Scatter plot for Price vs Cylinders
st.subheader('Scatter Plot: Price vs Cylinders')
st.plotly_chart(px.scatter(filtered_df, x='cylinders', y='price', title=f'Price vs Cylinders for Condition: {condition_filter}'))

‹#Box Plot: Replacing 'manufacturer' with 'model' or any other existing column
st.subheader('Box Plot: Price Distribution by Model')
st.plotly_chart(px.box(filtered_df, x='model', y='price', title=f'Price Distribution by Model for Condition: {condition_filter}'))

