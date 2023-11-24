import json
import requests
import base64
from Post import Post
from time import sleep

class Api:
    def __init__(self, credentials):
        self.__session = requests.Session()
        self.__auth_b64_string = base64.b64encode(
            f"{credentials['username']}:{credentials['api-key']}".encode('utf-8')).decode('utf-8')
        self.__session.headers.update({"Authorization": f"Basic {self.__auth_b64_string}",
                          "User-Agent": "e621-api/1.0.0 (by Furglacia on e621)"})

    status_codes = {
      "200": "OK - Request was successful",
      "204": "No Content - Request was successful, nothing will be returned. Most often encountered when deleting a record",
      "403": "Forbidden - Access denied. May indicate that your request lacks a User-Agent header (see Notice #2 above)",
      "404": "Not Found - Not found",
      "412": "Precondition failed",
      "420": "Invalid Record - Record could not be saved",
      "421": "User Throttled - User is throttled, try again later",
      "422": "Locked - The resource is locked and cannot be modified",
      "423": "Already Exists - Resource already exists",
      "424": "Invalid Parameters - The given parameters were invalid",
      "500": "Internal Server Error - Some unknown error occurred on the server",
      "502": "Bad Gateway - A gateway server received an invalid response from the e621 servers",
      "503": "Service Unavailable - Server cannot currently handle the request or you have exceeded the request rate limit. Try again later or decrease your rate of requests",
      "520": "Unknown Error - Unexpected server response which violates protocol",
      "522": "Origin Connection Time-out - CloudFlare's attempt to connect to the e621 servers timed out",
      "524": "Origin Connection Time-out - A connection was established between CloudFlare and the e621 servers, but it timed out before an HTTP response was received",
      "525": "SSL Handshake Failed - The SSL handshake between CloudFlare and the e621 servers failed"
    }

    def _eval_http_status(response, is_json: bool = True):
        if not response.ok:
            print(f"[{response.status_code}] \"{response.url}\": {Api.status_codes[f'{response.status_code}']}")
            quit()
        else:
            sleep(.55)  # sleep to not go over the speed limit (2r/s)
            print(f"[{response.status_code}] \"{response.url}\"")
            return json.loads(response.content) if is_json else response.content

    def get_posts(self, fetch_all: bool = False, page: int = 1, limit: int = 250, query: str = ""):
        if fetch_all:
            posts = []
            last_amount = -1
            while len(posts) != last_amount:
                last_amount = len(posts)
                position = f"limit={limit}&page={page}"
                posts += Api._eval_http_status(self.__session.get(f"https://e621.net/posts.json?{position}&{query}"))['posts']
                print(f"{position}: {len(posts)}")
                page += 1
            return [Post(post) for post in posts]
        else:
            position = f"limit={limit}&page={page}"
            return Api._eval_http_status(self.__session.get(f"https://e621.net/posts?{position}&{query}"))

    def download_post(self, post: Post, quality: int=0):  # quality: 0-preview 1-sample 2-full
        url = post.file['url'] if quality == 2 else post.sample['url'] if quality == 1 else post.preview['url']
        filename = f"{post.file['md5']}.{post.file['ext']}"
        with open(f"./Downloads/{filename}", "wb+") as file:
            file.write(Api._eval_http_status(self.__session.get(url), is_json=False))