from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


bbc_r = requests.get("https://www.bbc.com/news")
bbc_soup = BeautifulSoup(bbc_r.content, 'lxml')

bbc_headings = bbc_soup.find_all('a', {"class": "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"})

bbc_headings = bbc_headings[0:-13] # removing footers

bbc_news = []

for th in bbc_headings:
    bbc_news.append(th.text)





def index(request):
    return render(request, 'index.html', {'bbc_news':bbc_news})