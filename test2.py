
import lxml.html
import requests
import bs4
page = requests.get('http://jpm.jpmanga.space/')
webpage = lxml.html.fromstring(page.content)

a = webpage.xpath("//a[contains(@rel, 'nofollow')]/@href")
# a = webpage.xpath("//*[@id='aw0']/@href") for ads

print(a)

# import lxml.html
# import requests
# import bs4
# html = requests.get('http://jpm.jpmanga.space/')

# soup = bs4.BeautifulSoup(html.text, "lxml")

# ads_div = soup.find('div', attrs={'class': 'textwidget'})
# link = []
# if ads_div:
#     for link in ads_div.find_all('a', attrs={'id': 'aw0'}):
#         link.append( link['href'])

# print(link)



# import requests
# import lxml.html
# import bs4

# page = requests.get('http://jpm.jpmanga.space/')
# soup = bs4.BeautifulSoup(page.text, "lxml")

# # for link in soup.find_all('id="aw0"',href= True):
# #     print(link['href'])

# soup.find_all('a')
# webpage = lxml.html.fromstring(page.content)

# a = webpage.findAll("//*[@id='aw0']/@href")

# print(page.text)


# import requests
# import lxml
# import bs4


# page = requests.get('http://jpm.jpmanga.space/')
# soup = bs4.BeautifulSoup(page.text, "lxml")
# data = soup.findAll("//*[@id='aw0']/@href")

# for link in data:
#     print(link['href'])