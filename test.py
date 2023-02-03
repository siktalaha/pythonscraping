import requests
from bs4 import BeautifulSoup

import requests

response = requests.get(
  url='https://proxy.scrapeops.io/v1/',
  params={
      'api_key': 'xxxxxxxxxxxx',
      'url': 'https://www.amazon.in/s?k=bags',}
)

# print('Response Body: ', response.content)
soup=BeautifulSoup(response.content,"html.parser")
print(soup.title)
links=[]
texts=[]
for el in soup.find_all("h2",{"class": ["a-section","a-spacing-small","a-spacing-top-small","puis-padding-right-small","s-title-instruction-size","sg-col-inner","a-spacing-none","a-size-mini","s-line-clamp-2"]}):
    texts.append(el.find('span').get_text())
    links.append(el.find('a'))
    

print("Links are",links[:34])
print("Texts are",texts[:34])
# img_urls=[]
for el in soup.find_all("div",{'class':["a-section","aok-relative","s-image-fixed-height"]}):
    print(1,el["img"])
# ratings=[]
# for el in soup.find_all("i",{"class":["sg-col-inner","a-section","a-spacing-small","a-spacing-top-small","a-row","a-size-small","a-icon","a-icon-star-small-5","a-declarative"]}):
#     ratings.append(el.find('span',attrs={"class":"a-icon-alt"}))
# rating_list = list(filter(None,ratings))
# print(len(rating_list))
# number_review=[]
# for el in soup.find_all("span",{"class":["sg-col-inner","a-section","a-spacing-small","a-spacing-top-small","a-row","a-size-small","a-link-normal","s-underline-text","s-underline-link-text","a-size-base","s-underline-text"]}):
#     number_review.append(el)
# print(number_review[:34])
     

  