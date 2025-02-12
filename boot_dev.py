import random

class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]
    def __init__(self):
        self.__cards = self.create_deck()

    def create_deck(self):
        result = []
        for suit in DeckOfCards.SUITS:
            for rank in DeckOfCards.RANKS:
                card = (rank, suit)
                result.append(card)
        return result

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        if len(self.__cards) > 0:
            card = self.__cards[-1]
            self.__cards.pop()
            return card
        else:
            return None

    # don't touch below this line

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"


def main():
    a = DeckOfCards()
    a.shuffle_deck()

    for _ in range(0, 53):
        card = a.deal_card()
        print(card)



main()