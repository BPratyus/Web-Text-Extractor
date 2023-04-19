import requests
from bs4 import BeautifulSoup

url = input("https://www.dictionary.com/browse/review")

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
text = soup.get_text()

print(text)
