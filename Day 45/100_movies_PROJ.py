from requests import get
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

with get(url=URL) as response:
    soup = BeautifulSoup(response.text, 'html.parser')

movie_titles = [movie.getText() for movie in soup.find_all(name='h3', class_='title')][::-1]  # flip array with slicing

with open(file='movies.txt', mode='w', encoding='utf-8') as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")
