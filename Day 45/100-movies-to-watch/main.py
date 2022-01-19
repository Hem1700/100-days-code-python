from os import name
import re
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
website_html = response.text

soup = BeautifulSoup(website_html , 'html.parser')

all_movies = soup.find_all(name = 'h3' , class_ = 'title')
movie_title = [movie.getText() for movie in all_movies]
movies = movie_title[::-1]

with open("movies.txt" , 'w') as file:
    for movie in movies:
        file.write(f"{movie}\n")

