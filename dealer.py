import sys

from deck import Deck
from player import Player


class Dealer(Player):
    """Dealer of the game. A game has only one dealer.

    Attributes:
        player_name (str): The name of the dealer, i.e. 'Dealer'.
        hands (:obj:`list` of :obj:`Card`): The dealer's hands of cards.
        deck (:obj:`Deck`): The deck of the game. The dealer manages the deck.
        is_bust (bool): True if the dealer busts, False otherwise.
        score (int): The dealer's score.
        is_dealer_turn_started (bool): True if the dealer's turn has started, False otherwise.

    """

    def __init__(self):
        """Constructs an instance of Dealer.

        The dealer shuffles the deck at the beginning of the game.

        """
        self.player_name = "Dealer"
        self.hands = []
        self.deck = Deck()
        self.deck.shuffle()
        self.is_bust = False
        self.score = 0
        self.is_dealer_turn_started = False

    def deal_cards_for_initiation(self, game):
        """Deals cards at the beginning of the game.

        The dealer gives 1 card face-up to all players and 1 card face-up
        to themself. The dealer then gives 1 card face-up to all players,
        and 1 card face-down to themself. The hands of cards and initial
        score are updated for each player. The game automatically ends if
        the number of cards required by the players exceeds the number of
        cards in the deck.

        Args:
            game (:obj:`Game`): The instance of Game. Used to update each
                player's hands and score.

        Raises:
            ValueError: If the number of cards required by the players
                exceeds the number of cards in the deck, the game ends.

        """
        try:
            total_player_num = len(game.all_players)
            cards_to_deal = total_player_num * 2

            if cards_to_deal > len(self.deck):
                raise ValueError("Too many players and not enough card. The game ends.")

            for player in game.all_players:
                player.hands.append(self.deck.deal_card())
            for player in game.all_players:
                player.hands.append(self.deck.deal_card())
                player.initiate_score()

            self.initiate_score()

        except ValueError as too_many_players_error:
            print(too_many_players_error)
            sys.exit(1)

    def deal_cards_for_hit(self, game, player_index):
        """Deals card whenever a player hits.

        Args:
            game (:obj:`Game`): The instance of Game. Used to update
                player's hand and score.
            player_index (int): The index of the player who hits in the
                all_players list.

        Raises:
            RuntimeError: If the cards run out, the game ends.

        """
        try:
            if len(self.deck) == 0:
                raise RuntimeError("We run out of cards. The game ends.")

            card_to_deal = self.deck.deal_card()
            game.all_players[player_index].hands.append(card_to_deal)
            game.all_players[player_index].update_score()

            print(game.all_players[player_index].player_name + " got a new card: " + str(card_to_deal))
            print(game.all_players[player_index].player_name + "'s current score: " + str(game.all_players[player_index].score))

        except RuntimeError as no_card_error:
            print(no_card_error)
            sys.exit(1)

    def get_decision(self, game):
        """Gets the decision of dealer and takes corresponding actions in the dealer's turn.

        If the dealer's initial hands has a score < 17, then the dealer
        needs to continuously hit until their score >= 17. If the dealer's
        score ever > 21, the dealer busts.

        Args:
            game (:obj:`Game`): The instance of Game. Used to change the
                attributes of dealer in the game.

        """
        while self.score < 17:
            print("Dealer needs to hit (current score < 17)")
            self.deal_cards_for_hit(game, -1)

        if self.score > 21:
            self.is_bust = True
            print(self.player_name + " BUST!")