from Forum import players, fortress


class Forum(object):
    def __init__(self, session, mcgl):
        self.players = players.Players(session, mcgl)
        self.fortress = fortress.Fortress(session, mcgl)
        # self.production = production.Production(self.session)
        # self.top = top.Top(self.session)
        # self.bans = bans.Bans(self.session)
        # self.mutes = mutes.Mutes(self.session)
        # self.clans = clans.Clans(self.session)
        # self.fortress = fortress.Fortress(self.session)
