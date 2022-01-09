from bs4 import BeautifulSoup as bs


class Players(object):
    def __init__(self, session, mcgl):
        self.session = session
        self.mcgl = mcgl

    @staticmethod
    def _get_user_clan_info(user_page):
        info = {}
        for block in bs(user_page, 'html.parser').find_all('div', class_='profile-block'):
            block_name = block.find('div', class_='head').text
            if block_name == 'Клан':
                clan_name = block.a.text
                clan_pos = block.find('span', class_='value').text.replace('\t', '').replace('\n', '')
                clan_url = block.a['href']
                info = {'Клан': clan_name, 'Должность': clan_pos, 'Ссылка на клан': clan_url}
        return info

    @staticmethod
    def _get_user_general_info(user_page):
        res = {}
        for block in bs(user_page, 'html.parser').find_all('div', class_='profile-block'):
            block_name = block.find('div', class_='head').text
            info = []
            if block_name == 'Сообщества':
                for item in block.find_all('span', class_='team-link'):
                    team_link = item.a['href']
                    team_name = item.a.text
                    info.append({team_name: team_link})
                res[block_name] = info

            elif block_name == 'Ежедневные достижения':
                for item in block.find_all('tr'):
                    achieve_name = item.find('td', class_='text-row').text.replace('\t', '').replace('\n', '')
                    achieve_date = item.find('td', class_='author-row',
                                             style='white-space:nowrap;').text.replace('\t', '').replace('\n', '')
                    info.append({achieve_name: achieve_date})
                res[block_name] = info

            elif block_name == 'Клан':
                clan_name = block.a.text
                clan_pos = block.find('span', class_='value').text.replace('\t', '').replace('\n', '')
                clan_url = block.a['href']
                info.append({'Клан': clan_name, 'Должность': clan_pos, 'Ссылка на клан': clan_url})
                res[block_name] = info

            elif block_name == 'Аватар':
                if block.find('div', class_='item').text == "":
                    res[block_name] = {block_name: block.img['src']}
                else:
                    res[block_name] = {block_name: block.find('div', class_='item').text}

            else:
                for item in block.find_all('div', class_='item'):
                    title = item.find('span', class_='title').text.replace('\t', '').replace('\n', '')
                    value = item.find('span', class_='value').text.replace('\t', '').replace('\n', '')
                    info.append({title: value})
                res[block_name] = info
        return res

    def get_user_by_id(self, user_id: int):
        resp = self.session.get('https://forum.minecraft-galaxy.ru/profilemain/' + user_id)
        return self._get_user_general_info(resp.text)

    def get_user_by_nickname(self, nickname: str):
        resp = self.session.post('https://forum.minecraft-galaxy.ru/users/', data={'form': '',
                                                                                   'search': '',
                                                                                   'login': nickname})
        user_id = bs(resp.text).find('td', class_='text-row').a['href']
        resp = self.session.get('https://forum.minecraft-galaxy.ru' + user_id)
        return self._get_user_general_info(resp.text)

    def get_user_clan_by_id(self, user_id: int):
        resp = self.session.get('https://forum.minecraft-galaxy.ru/profilemain/' + user_id)
        return self.__get_user_clan_info(resp.text)
