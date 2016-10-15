import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

base_url = "http://xkcd.com/"

for n in range(1, 3):
    url = base_url + str(n)
    page = requests.get(url).content
    soup = BeautifulSoup(page, "lxml")
    comicImageBlock = soup.find("div",{"id":"comic"})
    comicImageTag = comicImageBlock.find("img")
    comicURL = comicImageTag['src']
    imageURL = 'https:' + comicURL
    img_data = requests.get(imageURL)
    i = Image.open(BytesIO(img_data.content))
    save_file_name = 'xkcd' + str(n) + '.png'
    i.save(save_file_name)