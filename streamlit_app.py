import streamlit
import pandas 
import requests

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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)


##New section for API response
streamlit.header("Fruityvice Fruit Advice!")

##Add API conection
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
#streamlit.text(fruityvice_response.json()) #writes data to screen in Json format

# transform data to pandas df
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# display table data on screen
streamlit.dataframe(fruityvice_normalized)
