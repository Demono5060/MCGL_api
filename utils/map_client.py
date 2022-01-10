class MapClient:
    def __init__(self, session):
        self.session = session
        self.domain = "map.minecraft-galaxy.ru"

    def get(self, url, params=None):
        return self.session.get("https://"+self.domain+url, params=params)
