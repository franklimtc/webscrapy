import urllib.request
from bs4 import BeautifulSoup
import csv

fp = urllib.request.urlopen("https://www.bbc.com")
htmlPage = fp.read()

mystr = htmlPage.decode("utf8")
fp.close()


# with open(htmlPage) as fp1:
#     soup = BeautifulSoup(fp1, 'html.parser')
# print(mystr)
soup = BeautifulSoup(mystr, 'html.parser').body
# type(tag)
# teste = soup.find_all(string='media-list')

mydivs = soup.findAll("div", {"class": "media"})
# print(mydivs)


with open('news.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['titulo', 'source', 'summary', 'link'])
    # print('titulo, source, summary, link')

    for div in mydivs:
        #print('Titulo: ', div['data-bbc-title']) #OK
        titulo =  div['data-bbc-title'] 
        #print('Source: ', div['data-bbc-source']) #OK
        source = div['data-bbc-source']
        
        summary = div.find("p", {"class": "media__summary"})
        if summary:
            summary = summary.string.strip()
            #print('Summary: ', summary.string.strip())
        else:
            summary = ''
        
        try:
            alink = div.find("a", {"class": "media__link"})
            
            if 'www.bbc.com' not in alink.get('href'):
                # print('URL: https://www.bbc.com' + alink.get('href')) #OK
                link = 'https://www.bbc.com' + alink.get('href')
            if 'www.bbc.com' in alink.get('href'):
                # print(alink.get('href'))
                link = alink.get('href')
                
        except:
            alink = div.find("a", {"class": "reel__link"})
            
            if 'www.bbc.com' not in alink.get('href'):
                # print('URL: https://www.bbc.com' + alink.get('href')) #OK
                link = 'https://www.bbc.com' + alink.get('href')
                
            if 'www.bbc.com' in alink.get('href'):
                # print(alink.get('href')) #OK
                link = alink.get('href')
                
        
        # print(titulo + ',' +  source + ',' +  summary + ',' +  link)       
        writer.writerow([titulo, source, summary, link])
        
        # soup2 = BeautifulSoup(div, 'html.parser')
        # mydivs2 = soup2.findAll("div", {"class": "media__content"})
        # print(soup2)
        