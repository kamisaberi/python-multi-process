import requests
import random
import string

with  (links := open('links.txt', "rt", encoding="utf8")):
    for link in links:
        ext = link.strip().split("/")[-1].strip().split("?")[0].strip().split(".")[-1]
        content = requests.get(link).content
        name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        with open("files/single/" + name + "." + ext, "wb") as file:
            file.write(content)
