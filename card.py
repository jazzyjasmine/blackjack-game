class Card:
    """A single card in a deck.

    Attributes:
            rank (str): The rank of the card, eg. 'J', 'Q', '2'.
            suit (str): The suit of the card, eg. 'Spades', 'Clubs', 'Diamonds'.

    """

    def __init__(self, rank, suit):
        """Constructs an instance of Card.

        Args:
            rank (str): The rank of the card, eg. 'J', 'Q', '2'.
            suit (str): The suit of the card, eg. 'Spades', 'Clubs', 'Diamonds'.

        """
        self.rank = rank
        self.suit = suit

    def __str__(self):
        """Represents an instance of Card as string.

        Returns:
            str: The string representation of an instance of Card.
        """
        return "{} of {}".format(self.rank, self.suit)

    @staticmethod
    def rank_to_score_except_ace(rank):
        """A statics methods that converts a non-Ace rank to a score.

        The rank through '2' to '10' are scored by face value. The rank of
        'J', 'Q', and 'K' are all scored as 10.

        This function does not evaluate a rank of 'A' because in this
        game 'A' can be either 1 or 11 depending on different situations.
        We specifically handle the rank of 'A' when calculating the score
        (see Player.initiate_score(self) and Player.update_score(self)
        methods).

        Args:
            rank (str): A non-Ace rank of the card.

        Returns:
            int: The score of a given non-Ace rank.

        Raises:
            ValueError: If `rank` is an 'A'.
        """
        try:
            if rank == 'A':
                raise ValueError("This function does not evaluate rank of A")
            if rank in ('J', 'Q', 'K'):
                return 10
            return int(rank)
        except ValueError as ace_error:
            print(ace_error)