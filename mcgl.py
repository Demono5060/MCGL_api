from requests import Session
from forum import Forum
from map import Map
from utils.map_client import MapClient
from utils.forum_client import ForumClient
from bs4 import BeautifulSoup as bs


class MCGL(object):
    def __init__(self, login=None, password=None, fcode=None, recap=None):
        self.login = login
        self.password = password
        self.fcode = fcode
        self.recap = recap
        self.session = Session()
        self.session.headers.update({'User-Agent': 'MCGL_API'})
        self.auth()
        self.forum = Forum(self)
        self.map = Map(self)
        self.map_client = MapClient(self)
        self.forum_client = ForumClient(self)

    def auth(self):
        if not self.login:
            raise Exception('Login is required to auth')

        self.session.get('https://forum.minecraft-galaxy.ru/guilogin/')
        self.session.post('https://forum.minecraft-galaxy.ru/login.php', data={
            'login': self.login,
            'pass': self.password,
            'fcode': self.fcode,
            'recap': self.recap
        })

    def is_logged_in(self):
        html = self.session.get('https://forum.minecraft-galaxy.ru/main/')
        if bs(html.text, 'html.parser').find('div', class_='button-container').a['href'] == "/guilogin/":
            return False
        return True
