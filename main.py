import json
from Api import Api
import os

with open("credentials.json") as file:
    credentials = json.loads(file.read())

api = Api(credentials)
api.get_favorites(fetch_all=True, download=True)

'''
for f in os.listdir("./Downloads/various stuff merge later/"):
    if f.split('.')[1] == "webm" or f.split('.')[1] == "png" or f.split('.')[1] == "mp4":
        if f.startswith("2021") or f.startswith("RDT"):
            continue
        f = f.removeprefix("sample_")
        f = f.split(".")[0]
        f = f.removesuffix("_480p")
        print(f)
        p = api.get_post_by_filename(f)
        if p != None:
            api.add_favorite(p)


all_favs = api.get_favorites(fetch_all=True)
for fav in all_favs:
    print(f"{fav.file['md5']}.{fav.file['ext']}")
    if f"{fav.file['md5']}.{fav.file['ext']}" in os.listdir("./Downloads/various stuff merge later/"):
        os.remove(f"./Downloads/various stuff merge later/{fav.file['md5']}.{fav.file['ext']}")
        print(f"Removed: {fav.file['md5']}.{fav.file['ext']}")
    if f"sample_{fav.file['md5']}.{fav.file['ext']}" in os.listdir("./Downloads/various stuff merge later/"):
        os.remove(f"./Downloads/various stuff merge later/sample_{fav.file['md5']}.{fav.file['ext']}")
        print(f"Removed: sample_{fav.file['md5']}.{fav.file['ext']}")
    if f"{fav.file['md5']}_480p.{fav.file['ext']}" in os.listdir("./Downloads/various stuff merge later/"):
        os.remove(f"./Downloads/various stuff merge later/{fav.file['md5']}_480p.{fav.file['ext']}")
        print(f"Removed: {fav.file['md5']}_480p.{fav.file['ext']}")
'''
print("done")

