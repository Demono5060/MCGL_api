from requests import Session
from forum import Forum


class MCGL(object):
    def __init__(self, login=None, password=None, fcode=None, recap=None):
        self.login = login
        self.password = password
        self.fcode = fcode
        self.recap = recap
        self.session = Session()
        self.session.headers.update({'User-Agent': 'MCGL_API'})
        self.auth()
        self.forum = Forum(self.session, self)

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
