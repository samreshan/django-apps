from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/section/technology"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# headings = soup.find_all('h3', class_="css-miszbp e1hr934v2")
headings = soup.find_all('a', class_="css-8hzhxf")

article_titles = []  # Create a list to store article titles
article_links = []  # Create a list to store article links
news = ""
for heading in headings:
    link = heading['href']  # Extract and strip the text content of the heading
    title = heading.h3.text # Extract the link associated with the heading
    article_titles.append(title)
    article_links.append(link)


def index(request):
    articles = zip(article_titles, article_links)

    context = {
        'articles': articles,
    }

    return render(request, 'newsBS/index.html', context)
