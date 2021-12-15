import sys

from player import HumanPlayer, ComputerPlayer
from dealer import Dealer


class Game:
    """The game itself.

    Attributes:
        dealer (:obj:`Dealer`): The dealer of the game.
        all_players (:obj:`list` of :obj:`Player`): A list of players, including human players,
            computer players and the dealer.

    """
    def __init__(self, num_human_player=1, num_computer_player=1):
        """Constructs an instance of Game.

        Args:
            num_human_player (int): The number of human players (default to be 1).
            num_computer_player (int): The number of computer players (default to be 1).

        Raises:
            ValueError: If the number of human player < 1 or the number of computer
                player < 1.
        """
        try:
            if num_human_player < 1 or num_computer_player < 1:
                raise ValueError("The game must have at least one human player and one computer player!")
            self.dealer = Dealer()
            self.all_players = [HumanPlayer(_) for _ in range(1, num_human_player + 1)]
            self.all_players.extend([ComputerPlayer(_) for _ in range(1, num_computer_player + 1)])
            self.all_players.append(self.dealer)
            self.dealer.deal_cards_for_initiation(self)
        except ValueError as player_num_error:
            print(player_num_error)

    def show_game_state(self):
        """Displays the game state.

        Displays each player as string, including player name,
        hands of cards, score, bust status, etc.

        Returns:
            str: The string representation of the game state.

        """
        print("Current Game State:")
        print("======================")
        all_players_string = ''.join(str(player) for player in self.all_players)
        print(all_players_string)

    def players_turn(self):
        """Starts the players' turn.

        Each player needs to decide whether hits or stands. If the player's score
        exceeds 21, they busts. Each player's turn ends either because they stands
        or they busts.

        """
        print("The players' turn starts.")
        for current_player_index, current_player in enumerate(self.all_players[:-1]):
            while current_player.score <= 21:
                decision_code = current_player.get_decision()
                if decision_code == 2:
                    print(current_player.player_name + " chose to stand")
                    break
                print(current_player.player_name + " chose to hit")
                self.dealer.deal_cards_for_hit(self, current_player_index)

            if current_player.score > 21:
                current_player.is_bust = True
                print(current_player.player_name + " BUST!\n")
        print("The players' turn ends.\n")

    def dealer_turn(self):
        """Starts the dealer's turn.

        The dealer reveals the face-down card and then stands if their score
        >= 17, otherwise they hits until their score >= 17. If the dealer's
        score ever exceeds 21, they busts.

        """
        print("Dealer's turn starts.")
        print("Dealer reveals the face-down card: " + str(self.dealer.hands[1]))
        print("Dealer's initial score is: " + str(self.dealer.score))
        self.dealer.is_dealer_turn_started = True
        self.dealer.get_decision(self)
        print("Dealer's final score: " + str(self.dealer.score))
        print("Dealer's turn ends.\n")

    def declare_result(self):
        """Declares the result of the game.

        First, find the players who do not bust. Then choose the highest score
        in these players. Players with the highest score are winners. If everyone
        busts, then there is no winner, i.e. everyone loses the game.

        When deciding the highest score, we only consider the rank.

        """
        potential_winners = list(filter(lambda player: not player.is_bust, self.all_players))
        if len(potential_winners) == 0:
            print("************ GAME RESULT ************")
            print("No winners! Everyone loses the game.\n")
            return
        max_score = max([player.score for player in potential_winners])
        winners = [player.player_name for player in potential_winners if player.score = max_score]
        # winners = list(map(lambda player: player.player_name,
        #                    filter(lambda player: player.score == max_score, potential_winners)))
        print("\n************ GAME RESULT ************")
        print("WINNER(S): " + ", ".join(winners) + '\n')

    @staticmethod
    def prompt_new_round():
        """Interactively prompts the human player if they wants to start new round or quits."""
        while True:
            try:
                message = "Want another around? 1-yes, 2-no\n"
                decision = int(input(message))
                if decision == 1:
                    print("A new round starts:\n")
                    game = Game()
                    game.play()
                elif decision == 2:
                    print("Bye-bye!")
                    sys.exit(1)
                else:
                    print("Invalid number. Please enter 1 or 2.")
            except ValueError:
                print("Invalid value. Please enter a valid choice.")
                continue

    def play(self):
        """Plays the game."""
        self.show_game_state()
        self.players_turn()
        self.dealer_turn()
        self.show_game_state()
        self.declare_result()
        Game.prompt_new_round()