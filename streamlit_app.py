import streamlit
import pandas 

##add title
streamlit.title('My Parents New Healthy Diner')

##add header 
streamlit.header('Breakfast Favorites')
##add text
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

##another header
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

##adding data from S3 bucket using pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
