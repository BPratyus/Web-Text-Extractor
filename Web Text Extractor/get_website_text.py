from langcodes import Language
from regex import P
import requests
from bs4 import BeautifulSoup
from newspaper import Article

url = "https://us.cnn.com/2023/04/19/us/dadeville-alabama-birthday-party-shooting-wednesday/index.html"

# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# text = soup.find('html')
# print(text)


# # print(text)
# print(soup.prettify())

article = Article(url,language="en")
article.download()
article.parse()
article.nlp()
print(article.title)
print(article.text)
print(article.summary)
print(article.keywords)

