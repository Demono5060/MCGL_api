import requests


class ForumClient:
    def __init__(self, mcgl):
        self.mcgl = mcgl
        self.session = self.mcgl.session
        self.domain = "forum.minecraft-galaxy.ru"

    def get(self, url, params=None):
        while True:
            if self.mcgl.is_logged_in():
                try:
                    return self.session.get("https://" + self.domain + url, params=params)
                except requests.exceptions.ConnectionError as err:
                    print(err.errno)
            else:
                self.mcgl.auth()
                try:
                    return self.session.get("https://" + self.domain + url, params=params)
                except requests.exceptions.ConnectionError as err:
                    print(err.errno)

    def post(self, url, data=None):
        while True:
            if self.mcgl.is_logged_in():
                try:
                    return self.session.get("https://" + self.domain + url, data=data)
                except requests.exceptions.ConnectionError as err:
                    print(err.errno)
            else:
                self.mcgl.auth()
                try:
                    return self.session.get("https://" + self.domain + url, data=data)
                except requests.exceptions.ConnectionError as err:
                    print(err.errno)
