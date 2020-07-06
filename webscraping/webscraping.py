import requests
import bs4
from pprint import pprint

#making calls 
results = requests.get("https://en.wikipedia.org/wiki/Mahatma_Gandhi")

#pprint(vars(results))

#beautifying the results source code
# it returns a soup object
soup = bs4.BeautifulSoup(results.text,"lxml")

print("******************")
print("\n")
#grabbing headers
print(soup.select('h1')[0].getText())
print("\n")
print("******************")
print("\n")


#grabbing images
allimages = soup.select('img')
print('https:'+allimages[0]['src'])
imglink = requests.get('https:'+allimages[0]['src'])
print(imglink.content)
f = open("myimg.png",'wb')
f.write(imglink.content)
f.close()
print("\n")
print("******************")
print("\n")


#grabbing classes
allclasses = soup.select('.mw-jump-link')
print(allclasses)