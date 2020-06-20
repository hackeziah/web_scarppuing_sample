
from lxml import html
import requests
from bs4 import BeautifulSoup
url = 'https://horriblesubs.info/shows/ballroom-e-youkoso/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.content, 'lxml')
a = soup.findAll("a",{"class": "dl-type hs-ddl-link"})

for link in a:
    print(link)

# import lxml.html
# import requests
# import bs4
# page = requests.get('https://horriblesubs.info/shows/ballroom-e-youkoso/')
# webpage = lxml.html.fromstring(html=page.text)

# soup = bs4.BeautifulSoup(page.text, "lxml")
# link = webpage.xpath("//*[@class='dl-type hs-ddl-link']/a/@href")
# print(link)


# import lxml.html
# import requests
# import bs4
# page = requests.get('http://jpm.jpmanga.space/')
# webpage = lxml.html.fromstring(page.content)
# a = webpage.xpath("//*[@class='dl-type hs-ddl-link']/a/@href")

# print(a)


# from lxml import html
# import requests

# url = 'https://horriblesubs.info/shows/ballroom-e-youkoso/'
# response = requests.get(url)
# tree = html.fromstring(response.content)
# obj = tree.xpath("//*[@class='dl-type hs-ddl-link']/a/@href")
# links = {
#     'links-update':obj
# }
# print(links)

# from lxml import html
# import requests

# page = requests.get('https://horriblesubs.info/shows/ballroom-e-youkoso/')
# webpage = html.fromstring(page.content)

# a=  webpage.xpath("//*[@class='dl-type hs-ddl-link']/a/@href")

# # total_tags = []
# # for tag in a:
# #     total_tags.append(tag)

# print(a)

#e for i in obj:
    # print(i.text)
# data =  sum(int(i.text) for i in obj)

# print(f'The sum of all count is doc is: {data}')
# from lxml import html
# import requests
# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# page = requests.get('https://horriblesubs.info/shows/ballroom-e-youkoso/')
# webpage = html.fromstring(page.content)

# a =webpage.xpath("//*[@class='dl-type hs-ddl-link']/a/@href")

# print(a)




# from lxml import html
# import requests
# page = requests.get('https://horriblesubs.info/shows/ballroom-e-youkoso/')
# tree = html.fromstring(page.text)

# data = tree.xpath("//*[@class='dl-type hs-ddl-link']/a/@href")

# print(data)