class MapClient:
    def __init__(self, mcgl):
        self.mcgl = mcgl
        self.session = self.mcgl.session
        self.domain = "map.minecraft-galaxy.ru"

    def get(self, url, params=None):
        if self.mcgl.is_logged_in():
            return self.session.get("https://"+self.domain+url, params=params)
        else:
            self.mcgl.auth()
            return self.session.get("https://"+self.domain+url, params=params)
