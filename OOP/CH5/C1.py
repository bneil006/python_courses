# could use the random library here and draw cards at random to battle head to head

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(self.rank)
        self.suit_index = SUITS.index(self.suit)

    def __eq__(self, other):
        if other.rank_index == self.rank_index and other.suit_index == self.suit_index:
            return True
        return False

    def __lt__(self, other):
        if self.rank_index < other.rank_index:
            return True
        elif self.rank == other.rank and self.suit_index < other.suit_index:
            return True
        return False

    def __gt__(self, other):
        if self.rank_index > other.rank_index:
            return True
        elif self.rank == other.rank and self.suit_index > other.suit_index:
            return True
        return False

    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    

def main():
    card1 = Card(RANKS[12], SUITS[2])
    card2 = Card(RANKS[10], SUITS[2])

    print(f"RANK: {card1.rank}, SUIT: {card1.suit}, RANK INDEX: {card1.rank_index}, SUIT INDEX: {card1.suit_index}")
    print(f"RANK: {card2.rank}, SUIT: {card2.suit}, RANK INDEX: {card2.rank_index}, SUIT INDEX: {card2.suit_index}")

    print(card1 == card2)
    print(card1 < card2)
    print(card1 > card2)
    

main()