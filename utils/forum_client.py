class ForumClient:
    def __init__(self, session):
        self.session = session
        self.domain = "forum.minecraft-galaxy.ru"

    def get(self, url, params=None):
        return self.session.get("https://"+self.domain+url, params=params)

    def post(self, url, data=None):
        return self.session.post("https://"+self.domain+url, data=data)
