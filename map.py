import json
import base64


class Map(object):
    def __init__(self, session, mcgl):
        self.session = session
        self.mcgl = mcgl

    def get_systems(self):
        systems = self.session.get("https://map.minecraft-galaxy.ru/systems/")
        systems = json.loads(systems.text)
        res = {}
        for i in systems:
            system = {i['name'].replace('Survival', 'Nano').replace('Advance', 'Zeus'): i['id']}
            res.update(system)
        return res

    def get_players(self, server_id):
        f = 'http://map.minecraft-galaxy.ru/players/' + str(server_id) + '?d=0&filter=2&recap='
        self.session.get('https://map.minecraft-galaxy.ru/#0/0/12/0/43/')
        resp = self.session.get(f).text.replace("{\"players\":", "").replace(",\"error\":2}", "") \
            .replace(",\"error\":0}", "")
        players = json.loads(resp)
        return players

    def get_zone_info(self, w, x, z):
        resp = self.session.get('https://map.minecraft-galaxy.ru/zoneinfo/?w=' + str(w) + '&x=' + str(x) + '&y=' + str(z))
        info = json.loads(base64.b64decode(resp.text))
        return info