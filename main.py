import json
from Api import Api

with open("credentials.json") as file:
    credentials = json.loads(file.read())

api = Api(credentials)
r = api.get_posts(fetch_all=True, query="tags=calvin_mcmurray")
print(f"Final amount: {len(r)}")

tmp = [api.download_post(post, quality=2) for post in r]

print("done")

