# Scraping 100 Movies

from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website = response.text

soup = BeautifulSoup(website, "html.parser")

movie_titles = []

main_heading = soup.find_all(name="h3", class_="title")

for heading in main_heading:
    title = heading.getText()
    movie_titles.append(title)

# Reversed List
movie_titles.reverse()

for title in movie_titles:
    with open("movies.txt", mode="a", encoding="utf-8-sig") as f:
        f.write(f"{title}\n")
