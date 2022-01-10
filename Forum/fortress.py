from bs4 import BeautifulSoup as bs


class Fortress(object):
    def __init__(self, mcgl):
        self.mcgl = mcgl

    def get_fortress_logs_list(self, fortress_id):
        content = self.mcgl.forum_client.get('/fortresshistory/'+fortress_id)
        logs = []
        for block in bs(content.text, 'html.parser').find_all('tr'):
            block_info = {}
            if block.find('td', class_="text-row"):
                block_info['clan'] = block.find('td', class_="text-row").a.text
                block_info['date'] = block.find('td', class_="author-row").text
                block_info['url'] = block.find_all_next("a")[1]['href']
                logs.append(block_info)
        return logs

    def get_fortress_list(self):
        content = self.mcgl.forum_client.get('/fortress/')
        fortress = []
        for block in bs(content.text, 'html.parser').find_all('tr'):
            block_info = {}
            if block.find('td', class_='text-row'):
                a = block.find_all_next('a')
                block_info['fortress_name'] = a[0].text
                block_info['fortress_url'] = a[0]['href']
                block_info['fortress_coord'] = a[1].text
                block_info['map_url'] = a[1]['href']
                block_info['clan_owner'] = a[2].text
                block_info['clan_owner_url'] = a[2]['href']
                block_info['server_name'] = a[3].text
                block_info['server_url'] = a[3]['href']
                fortress.append(block_info)
        return fortress

    def get_fortress_log_pvp(self, log_url):
        content = self.mcgl.forum_client.get(log_url, {'t': '6'})
        log = []
        for block in bs(content.text, 'html.parser').find_all('table', class_="bc_table"):
            for tr in block.find_all('tr', class_=['bc_row_1', 'bc_row_0']):
                info = {}
                td = tr.find_all('td')
                info['nickname'] = td[0].text
                info['clan'] = td[1].text
                info['side'] = td[2].text
                info['race'] = td[3].text
                info['prof'] = td[4].text
                info['kills'] = td[5].text
                info['death'] = td[6].text
                log.append(info)
        return log

    def get_fortress_log_capture(self, log_url):
        content = self.mcgl.forum_client.get(log_url, {'t': '3'})
        log = []
        for block in bs(content.text, 'html.parser').find_all('table', class_="topics"):
            for tr in block.find_all('tr'):
                info = {}
                if tr.find_all('td', class_=['author-row', "text-row"]):
                    td = tr.find_all('td', class_=['author-row', "text-row"])
                    info['time'] = td[0].text
                    info['nickname'] = td[1].text
                    info['clan'] = td[2].text
                    info['event'] = td[3].text
                    log.append(info)
        return log
