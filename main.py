import json
from Api import Api
import os
import hashlib

with open("credentials.json") as file:
    credentials = json.loads(file.read())



api = Api(credentials)
api.sync_favorites()


all_favs = api.get_favorites(fetch_all=True)
for fav in all_favs:
    print(f"{fav.file['md5']}.{fav.file['ext']}")
    if f"{fav.file['md5']}.{fav.file['ext']}" in os.listdir("./Downloads/undetectable/"):
        os.remove(f"./Downloads/undetectable/{fav.file['md5']}.{fav.file['ext']}")
        print(f"Removed: {fav.file['md5']}.{fav.file['ext']}")
    if f"{fav.file['md5']}.mp4" in os.listdir("./Downloads/undetectable/"):
        os.remove(f"./Downloads/undetectable/{fav.file['md5']}.mp4")
        print(f"Removed: {fav.file['md5']}.{fav.file['ext']}")
    if f"{fav.file['md5']}.png" in os.listdir("./Downloads/undetectable/"):
        os.remove(f"./Downloads/undetectable/{fav.file['md5']}.png")
        print(f"Removed: {fav.file['md5']}.{fav.file['ext']}")
    if f"{fav.file['md5']}.jpg" in os.listdir("./Downloads/undetectable/"):
        os.remove(f"./Downloads/undetectable/{fav.file['md5']}.jpg")
        print(f"Removed: {fav.file['md5']}.{fav.file['ext']}")
    if f"{fav.file['md5']}.webm" in os.listdir("./Downloads/undetectable/"):
        os.remove(f"./Downloads/undetectable/{fav.file['md5']}.webm")
        print(f"Removed: {fav.file['md5']}.{fav.file['ext']}")
    if f"{fav.file['md5']}.gif" in os.listdir("./Downloads/undetectable/"):
        os.remove(f"./Downloads/undetectable/{fav.file['md5']}.gif")
        print(f"Removed: {fav.file['md5']}.{fav.file['ext']}")
    if f"sample_{fav.file['md5']}.{fav.file['ext']}" in os.listdir("./Downloads/undetectable/"):
        os.remove(f"./Downloads/undetectable/sample_{fav.file['md5']}.{fav.file['ext']}")
        print(f"Removed: sample_{fav.file['md5']}.{fav.file['ext']}")
    if f"{fav.file['md5']}_480p.{fav.file['ext']}" in os.listdir("./Downloads/undetectable/"):
        os.remove(f"./Downloads/undetectable/{fav.file['md5']}_480p.{fav.file['ext']}")
        print(f"Removed: {fav.file['md5']}_480p.{fav.file['ext']}")

print("done")

