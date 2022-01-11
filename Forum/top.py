from bs4 import BeautifulSoup as bs


def parse_info(content):
    result = []
    for tr in bs(content.text, 'html.parser').find_all('tr'):
        top_info = {}
        td = tr.find_all('td', class_='author-row')
        if td:
            top_info['#'] = td[0].text
            top_info['username'] = td[1].a.text
            top_info['url'] = td[1].a['href']
            top_info['exchange'] = td[2].text
            top_info['prof'] = td[3].text
            top_info['created'] = td[4].text
            top_info['destroyed'] = td[5].text
            top_info['KCP'] = td[6].text
            top_info['passed'] = td[7].text
            top_info['death'] = td[8].text
            top_info['pvp'] = td[9].text
            top_info['pk'] = td[10].text
            top_info['played_time'] = td[11].text
            result.append(top_info)
    return result


class Top(object):
    def __init__(self, mcgl):
        self.mcgl = mcgl

    def get_top_exchange(self):
        content = self.mcgl.forum_client.get('/top/')
        return parse_info(content)

    def get_top_created(self):
        content = self.mcgl.forum_client.get('/top/'+'1')
        return parse_info(content)

    def get_top_destroyed(self):
        content = self.mcgl.forum_client.get('/top/'+'2')
        return parse_info(content)

    def get_top_passed(self):
        content = self.mcgl.forum_client.get('/top/'+'3')
        return parse_info(content)

    def get_top_death(self):
        content = self.mcgl.forum_client.get('/top/'+'4')
        return parse_info(content)

    def get_top_pvp(self):
        content = self.mcgl.forum_client.get('/top/'+'5')
        return parse_info(content)

    def get_top_pk(self):
        content = self.mcgl.forum_client.get('/top/'+'6')
        return parse_info(content)

    def get_top_played_time(self):
        content = self.mcgl.forum_client.get('/top/'+'7')
        return parse_info(content)
