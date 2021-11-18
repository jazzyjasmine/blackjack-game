from card import Card
import random


class Deck:
    """A 52-card deck.

    A deck has four suits: Spades, Diamonds, Clubs, Hearts. Each suit
    contains 13 ranks: Ace, 2 to 10, J, Q, K.

    Attributes:
        _cards (:obj:`list` of :obj:`Card`): A list of instances of Card.

    """

    def __init__(self):
        """Constructs an instance of Deck."""
        ranks = [str(n) for n in range(2, 11)]
        ranks += ["J", "Q", "K", "A"]
        suits = ["Spades", "Diamonds", "Clubs", "Hearts"]

        self._cards = []
        for suit in suits:
            for rank in ranks:
                self._cards.append(Card(rank, suit))

        random.shuffle(self._cards)

    def deal_card(self):
        """Deals one card from the deck.

        Returns:
            :obj:`Card`: The card to be dealt.

        """
        return self._cards.pop(0)

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self._cards)

    def __len__(self):
        """Gets the length of the deck, i.e. the number of cards.

        Returns:
            int: The length of the deck, i.e. the number of cards.

        """
        return len(self._cards)