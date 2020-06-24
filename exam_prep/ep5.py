#3.1
class Dress:
    """What color is the dress?
    >>> blue = Dress('blue')
    >>> blue.look()
    'blue'
    >>> gold = Dress('gold')
    >>> gold.look()
    'gold'
    >>> blue.look() # 2 does not evenly divide 3; changes to gold
    >>> Dress('black').look()
    'black'
    >>> gold.look() # 2 does not evenly divide 5; changes to black
    >>> gold.look() # 3 evenly divides 6
    'black'
    >>> Dress('white').look()
    'white'
    >>> gold.look() # 4 evenly divides 8
    'black'
    >>> blue.look() # 3 evenly divides 9
    'gold'
    """
    seen = 0
    color = None
    def __init__(self, color):
        self.color = color
        self.seen = 0
    def look(self):
        self.seen = self.seen + 1
        Dress.seen = Dress.seen + 1
        if Dress.seen % self.seen == 0:
            Dress.color = self.color
            return self.color
        else:
            self.color = Dress.color

#3.2
def play_round(starter, cards):
    """Play a round and return all winners so far. Cards is a list of pairs.
    Each (who, card) pair in cards indicates who plays and what card they play.
    >>> play_round(3, [(3, 4), (0, 8), (1, 8), (2, 5)])
    [1]
    >>> play_round(1, [(3, 5), (1, 4), (2, 5), (0, 8), (3, 7), (0, 6), (1, 7)])
    It's not your turn, player 3
    It's not your turn, player 0
    The round is over, player 1
    [1, 3]
    >>> play_round(3, [(3, 7), (2, 5), (0, 9)]) # Round is never completed
    It's not your turn, player 2
    [1, 3]
    """
    r = Round(starter)
    for who, card in cards:
        try:
            r.play(who, card)
        except AssertionError as e:
            print(e)
    return Round.winners

class Round:
    players, winners = 4, []
    def __init__(self, starter):
        self.starter, self.player, self.highest = starter, starter, -1
    def play(self, who, card):
        assert not self.complete(), 'The round is over, player '+str(who)
        assert who % 4 == self.player % 4, "It's not your turn, player "+str(who)
        self.player = who + 1
        if card >= self.highest:
            self.highest, self.control = card, who
        if who % 4 == self.starter % 4 - 1:
            self.winners.append(self.control)
    def complete(self):
        return self.player == self.starter and  self.highest != -1
