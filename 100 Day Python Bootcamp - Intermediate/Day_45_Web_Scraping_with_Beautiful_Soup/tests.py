from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = (response.text)

soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup)





# with open("website.html", mode="r", encoding="utf-8-sig") as f:
#     contents = f.read()

# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.p)


# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
    # print(tag.getText()) # # Gets all anchor tag texts - Strings
    # print(tag.get("href")) # # Getting the link value in href elements
    # pass

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)