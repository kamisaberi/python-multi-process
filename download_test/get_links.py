from bs4 import BeautifulSoup
import requests

web = requests.get("https://www.varzesh3.com")
soup = BeautifulSoup(web.content, "html.parser")
# print(soup.prettify())
images = soup.find_all("img")
extensions = ["jpg", "bmp", "png", "jpeg"]
with open("links.txt", "wt", encoding="utf8") as f1:
    for image in images:
        src = str(image["src"])
        ext = src.strip().split("/")[-1].strip().split("?")[0].strip().split(".")[-1]
        if ext in extensions:
            f1.write(image["src"] + "\n")
