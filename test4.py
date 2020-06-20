
from lxml import html
import requests
page = requests.get('http://www.mangago.me/read-manga/pendulum_kemonohito_omegaverse/')
tree = html.fromstring(page.content)

data = tree.xpath('//img[@class="showdesc loaded"]/@src')

print(data)



# import lxml.html
# import requests

# page = requests.get('http://www.mangago.me/read-manga/pendulum_kemonohito_omegaverse/')
# webpage = lxml.html.fromstring(page.text)

# a = webpage.xpath('//img[@class="showdesc loaded"]/@src')
# for atag in a:
#     print(atag)
