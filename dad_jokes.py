import streamlit as st
import requests
from bs4 import BeautifulSoup  

url='https://icanhazdadjoke.com/'
html = requests.get(url)

s = BeautifulSoup(html.content, 'html.parser')

results = s.find(class_='card')
jokes = results.find_all('p', class_='subtitle')

st.header('Dad Jokes Generator')

st.header(jokes[0].text)

if st.button('Refresh'):
    html = requests.get(url)

else:
    jokes = jokes
