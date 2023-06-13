import requests
from bs4 import BeautifulSoup
url="https://stackoverflow.com/questions/tagged/python"
response=requests.get(url)
soup=BeautifulSoup(response.content,"html.parser")
links=soup.find_all("a")
for link in links:
    print(link.text)


