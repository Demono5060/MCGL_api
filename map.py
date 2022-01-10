import json
import base64


class Map(object):
    def __init__(self, mcgl):
        self.mcgl = mcgl

    def get_systems(self):
        systems = self.mcgl.map_client.get('/systems')
        systems = json.loads(systems.text)
        res = {}
        for i in systems:
            system = {i['name'].replace('Survival', 'Nano').replace('Advance', 'Zeus'): i['id']}
            res.update(system)
        return res

    def get_players(self, server_id):
        self.mcgl.map_client.get('/#0/0/1/0/10/')
        resp = self.mcgl.map_client.get("/players/"+str(server_id), {'d': '0', 'filter': 2, 'recap': ''})
        players = json.loads(resp.text).get('players')
        return players

    def get_zone_info(self, w, x, z):
        resp = self.mcgl.map_client.get('/zoneinfo/', {'w': str(w), 'x': str(x), 'y': str(z)})
        info = json.loads(base64.b64decode(resp.text))
        return info