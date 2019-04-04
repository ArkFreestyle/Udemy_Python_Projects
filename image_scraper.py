from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os


def start_search():

    search = input("Search for:")
    params = {"q": search}
    dir_name = search.replace(" ", "").lower()

    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    r = requests.get("https://www.bing.com/images/search", params=params)

    soup = BeautifulSoup(r.text, "html.parser")

    links = soup.findAll("a", {"class": "thumb"})

    for item in links:
        try:
            image_object = requests.get(item.attrs["href"])
            print("Getting", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1]
            try:
                image = Image.open(BytesIO(image_object.content))
                image.save("./" + dir_name + "/" + title, image.format)
            except:
                print("Could not save image")
        except:
            print("Could not request.get the image")

    start_search()

start_search()
