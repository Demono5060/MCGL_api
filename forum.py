from Forum import players, fortress, top


class Forum(object):
    def __init__(self, mcgl):
        self.players = players.Players(mcgl)
        self.fortress = fortress.Fortress(mcgl)
        # self.production = production.Production(self.session)
        self.top = top.Top(mcgl)
        # self.bans = bans.Bans(self.session)
        # self.mutes = mutes.Mutes(self.session)
        # self.clans = clans.Clans(self.session)
        # self.fortress = fortress.Fortress(self.session)
