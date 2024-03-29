import requests
import random
import string
import os

if not os.path.exists("files/"):
    os.mkdir("files")
if not os.path.exists("files/single/"):
    os.mkdir("files/single/")

with  open('links.txt', "rt") as links:
    for link in links:
        ext = link.strip().split("/")[-1].strip().split("?")[0].strip().split(".")[-1]
        name = link.strip().split("/")[-1].strip().split("?")[0].strip().split(".")[0]
        content = requests.get(link.strip()).content
        # name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        with open(n := "files/single/" + name + "." + ext, "wb") as file:
            file.write(content)
            print(n)
        print(link)
