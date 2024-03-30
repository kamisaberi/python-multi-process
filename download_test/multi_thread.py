import os
import threading

import requests

if not os.path.exists("files/"):
    os.mkdir("files")
if not os.path.exists("files/multi/"):
    os.mkdir("files/multi/")


def download_image(link: str):
    ext = link.strip().split("/")[-1].strip().split("?")[0].strip().split(".")[-1]
    name = link.strip().split("/")[-1].strip().split("?")[0].strip().split(".")[0]
    content = requests.get(link.strip()).content
    # name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    with open(n := "files/multi/" + name + "." + ext, "wb") as file:
        file.write(content)
        print(n)
    print(link)


with  open('links.txt', "rt") as links:
    threads = []
    for link in links:
        th = threading.Thread(target=download_image, args=(link.strip(),))
        th.start()
        threads.append(th)
    for thread in threads:
        thread.join()
