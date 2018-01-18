from collections import defaultdict
from operator import itemgetter

class Card:
    RANKS = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

    def __init__(self, s):
        self.rank = Card.RANKS.index(s[0])
        self.suit = s[1]

    def __str__(self):
        return "%s%s" % (Card.RANKS[self.rank], self.suit)

class Hand:
    def __init__(self, cards):
        self.cards = sorted(cards, key=lambda c: c.rank)

    def flush(self):
        suit = self.cards[0].suit
        if all(card.suit == suit for card in self.cards[1:]):
            return suit

    def straight(self):
        last = self.cards[0].rank
        for card in self.cards[1:]:
            rank = card.rank
            if rank == last + 1: last = rank
            else: return None

        return self.cards[0].rank

    def sets(self):
        by_rank = defaultdict(lambda: [])
        for card in self.cards:
            by_rank[card.rank].append(card)


        by_size = defaultdict(lambda: [])
        for rank, cards in by_rank.items():
            by_size[len(cards)].append(rank)

        for l in by_size.values(): l.sort()

        return by_size


    def hands(self):
        flush = self.flush()
        straight = self.straight()

        # check straight flush
        # (note: royal flush is just the highest ranked straight flush)
        if flush is not None and straight is not None:
            yield (8, straight)

        sets = self.sets()

        # check four of a kind
        for rank in reversed(sets[4]):
            yield (7, rank)

        for three_rank in reversed(sets[3]):
            for two_rank in reversed(sets[2]):
                yield (6, three_rank, two_rank)

        if flush is not None:
            yield (5, tuple(sorted(self.cards, key=lambda c: c.rank, reverse=True)))

        if straight is not None:
            yield (4, straight)

        for rank in reversed(sets[3]):
            yield (3, rank)

        for rank in reversed(sets[2]):
            for other in reversed(sets[2]):
                if other != rank:
                    yield (2, rank, other)

        for rank in reversed(sets[2]):
            yield (1, rank)

        for card in sorted(self.cards, key=lambda c: c.rank, reverse=True):
            yield (0, card.rank)

    def compete(self, other):
        #print("{} v {}".format(self, other))
        for my_hand, other_hand in zip(self.hands(), other.hands()):

            if my_hand != other_hand:
                #if my_hand > other_hand:
                #    print("Player 1 wins with {}".format(my_hand))
                #else:
                #    print("Player 2 wins with {}".format(other_hand))
                return my_hand > other_hand

    def __str__(self):
        return "({})".format(",".join(map(str, self.cards)))


    @staticmethod
    def from_str(s):
        return Hand(map(Card, s.split()))


def test():
    assert Hand.from_str('5D 6D 7D 8D 9D').straight() == 3
    assert Hand.from_str('5H 5C 6S 7S KD').compete(Hand.from_str('2C 3S 8S 8D TD')) == False #Player 2
    assert Hand.from_str('5D 8C 9S JS AC').compete(Hand.from_str('2C 5C 7D 8S QH')) == True # Player 1
    assert Hand.from_str('2D 9C AS AH AC').compete(Hand.from_str('3D 6D 7D TD QD')) == False # Player 2
    assert Hand.from_str('4D 6S 9H QH QC').compete(Hand.from_str('3D 6D 7H QD QS')) == True # Player 1
    assert Hand.from_str('2H 2D 4C 4D 4S').compete(Hand.from_str('3C 3D 3S 9S 9D')) == True # Player 1

if __name__ == "__main__":
    with open('poker.txt', 'r') as fp:
        count = 0
        for line in fp:
            cards = list(map(Card, line.strip().split()))
            if Hand(cards[:5]).compete(Hand(cards[5:])):
                count += 1
        print(count)
