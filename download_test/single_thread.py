import requests
import random
import string

with  open('links.txt', "rt") as f1:
    links = f1.read().split("\n")
    for link in links:
        ext = link.strip().split("/")[-1].strip().split("?")[0].strip().split(".")[-1]
        name = link.strip().split("/")[-1].strip().split("?")[0].strip().split(".")[0]
        file_name = name + "." + ext
        print(file_name)
        content = requests.get(link).content
        # name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        with open(n := "files/single/" + file_name, "wb") as file:
            file.write(content)
            print(n)
        print(link)
