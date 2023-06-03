from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.





def search(request):
    if 'q' in request.GET:
        fars_list = []
        tasnim_list = []
        q = request.GET.get('q')
        sites = [f"https://search.farsnews.ir/?page=&t=all&b=Title&q={q}&o=on&from=&end=", f"https://www.tasnimnews.com/fa/search?query={q}&date=1"]
        
        for site in sites:
            search_r = requests.get(site)
            search_soup = BeautifulSoup(search_r.content, 'lxml')
            fars =  search_soup.find_all('h3', {"class": "mt-4"})
            tasnim =  search_soup.find_all('h2')
            
            for th in fars:
                fars_list.append(th.text)
            for th in tasnim:
                tasnim_list.append(th.text)
            

    return render(request, 'search.html', {'tasnim_list':tasnim_list,'fars_list':fars_list})




#   foori
foori_r = requests.get("https://www.khabarfoori.com/%D8%A8%D8%AE%D8%B4-%D8%A7%D9%82%D8%AA%D8%B5%D8%A7%D8%AF%DB%8C-145")
foori_soup = BeautifulSoup(foori_r.content, 'lxml')

foori_headings = foori_soup.find_all('a', {"target": "_blank"})

foori_headings = foori_headings[0:-13]

foori_news = []

for th in foori_headings:
    foori_news.append(th.text)
    
#    foori 


#   mash
mash_r = requests.get("https://www.mashreghnews.ir/service/economic-news")
mash_soup = BeautifulSoup(mash_r.content, 'lxml')

mash_headings = mash_soup.find_all('a', {"target": "_blank"})

mash_headings = mash_headings[0:-13]

mash_news = []

for th in mash_headings:
    mash_news.append(th.text)
    
#    mash     


 
 #   javan
javan_r = requests.get("https://www.yjc.ir/")
javan_soup = BeautifulSoup(javan_r.content, 'lxml')

javan_headings = javan_soup.find_all('a', {"class": "title-news-bartar"})



javan_news = []

for th in javan_headings:
    javan_news.append(th.text)
    
#    javan


 #   fars
fars_r = requests.get("https://www.farsnews.ir/economy")
fars_soup = BeautifulSoup(fars_r.content, 'lxml')

fars_headings = fars_soup.find_all('h3', {"class": "title d-block mb-2"})



fars_news = []

for th in fars_headings:
    fars_news.append(th.text)
    
#    fars     

    
def index(request):
    return render(request, 'index.html', {'foori_news':foori_news,'mash_news':mash_news,'javan_news':javan_news,
                                       'fars_news':fars_news   })
    
    
    





 #   tasnim
tasnim_r = requests.get("https://www.tasnimnews.com/fa/service/79/%D9%BE%D9%88%D9%84-%D8%A7%D8%B1%D8%B2-%D8%A8%D8%A7%D9%86%DA%A9")
tasnim_soup = BeautifulSoup(tasnim_r.content, 'lxml')

tasnim_headings = tasnim_soup.find_all('h2')



tasnim_news = []

for th in tasnim_headings:
    tasnim_news.append(th.text)
    
#    tasnim



#   mehr
mehr_r = requests.get("https://www.mehrnews.com/service/Economy")
mehr_soup = BeautifulSoup(mehr_r.content, 'lxml')

mehr_headings = mehr_soup.find_all('a',{"target": "_blank"})



mehr_news = []

for th in mehr_headings:
    mehr_news.append(th.text)
    
#    mehr    

def more(request):
    return render(request, 'more.html', {'tasnim_news':mehr_news,'mehr_news':tasnim_news  })

