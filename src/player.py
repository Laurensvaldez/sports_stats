# In this file you will find the classes of the players (or just class)

class Player:
    # create a method in the class
    def __init__(self, first, last, team, pos, games, atbats, runs, hits, doubles, triples, homeruns,
                 rbi, bb, so, sb, cs):
        # give the arguments
        self.first = first
        self.last = last
        self.team = team
        self.pos = pos
        self.games = games
        self.atbats = atbats
        self.runs = runs
        self.hits = hits
        self.doubles = doubles
        self.triples = triples
        self.homeruns = homeruns
        self.rbi = rbi
        self.bb = bb
        self.so = so
        self.sb = sb
        self.cs = cs
    # self.avg verwijderd (er is hieronder al een functie voor geschreven)

    # create a method in your class for the full name
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # create a method to determine average of hitters
    def average_hit(self):
        return self.hits/self.atbats