import requests
from bs4 import BeautifulSoup

def gather(keyword):
    url = "https://en.wikipedia.org/wiki/" + keyword
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    details = soup.find_all('table', {'class': 'infobox'})
    return details, soup('p')[:2]