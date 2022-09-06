from bs4 import BeautifulSoup
from requests import get

# # from file
# with open(file='website.html', mode='r', encoding="utf8") as file:
#     file_soup = BeautifulSoup(file.read(), 'html.parser')

# from website
with get(url="https://news.ycombinator.com") as response:
    web_soup = BeautifulSoup(response.text, 'html.parser')

articles = web_soup.find_all(name="a", class_="titlelink")
article_titles = []
article_links = []
article_upvotes = [int(article.getText().split()[0]) for article in web_soup.find_all(name="span", class_="score")]

for article in articles:
    article_titles.append(article.getText())
    article_links.append(article.get("href"))

highest_upvoted_index = article_upvotes.index(max(article_upvotes))

print(f"The current most popular article is '{article_titles[highest_upvoted_index]}', with "
      f"{article_upvotes[highest_upvoted_index]} upvotes.\nRead more at {article_links[highest_upvoted_index]}.")
