import random

from abc import ABC, abstractmethod
from card import Card


class Player(ABC):
    """A abstract class of Player. Denotes a general player in the game.

    A player can be a human player, a computer player, or dealer. They
    have a common behavior of making decision(stand or hit) in their turn.

    """

    @abstractmethod
    def get_decision(self, *args):
        """Prompts player's decision for their turn and takes according actions.

        Args:
            *args (optional): Arbitrary number of arguments
                related to decision-making.

        """
        pass

    def __str__(self):
        """Represents an instance of Player as string.

        Returns:
            str: The string representation of an instance of Player.
        """
        status_string = "Bust" if self.is_bust else "Not Bust"

        if self.player_name == "Dealer" and not self.is_dealer_turn_started:
            hands_string = str(self.hands[0]) + ", one face-down card"
        else:
            hands_string = ', '.join(str(card) for card in self.hands)

        return self.player_name + \
               "\nHands: " + hands_string + \
               "\nScore: " + str(self.score) + \
               "\nBust Status: " + status_string + \
               "\n======================\n"

    def initiate_score(self):
        """Calculates the player's initial score and updates the player's score attribute.

        Calculates the player's score after the dealing(before
        the players' turn starts) and updates the initial score
        to the player's score attribute.

        Logic of calculating the initial score:

        The initial score is an optimal score, i.e. the maximum
        score that is <= 21. After the dealing, each player has
        two cards, which contains the following three cases:

        Case #1: The two cards are both 'A'.
        The optimal score is 12 by letting one 'A' scoring 1 and
        the other 'A' scoring 11. The two 'A's can not both score
        11 because otherwise the total score would be 22, which
        exceeds 21 and triggers a bust. The two 'A's can not both
        score 1 because otherwise the total score would be 2, which
        is lower than 12.

        Case #2: The two cards contain only one 'A'.
        Let the single 'A' score 11 to achieve the optimal score. This
        will never trigger a bust because the possible maximum score
        of the other card is 10, however 10 + 11 = 21, which does not
        exceed 21 and thus will not trigger a bust.

        Case #3: The two cards contain no 'A'.
        Use the static method Card.rank_to_score_except_ace(rank) to
        get the score of each rank and then calculates the sum.

        """
        current_ranks = [current_card.rank for current_card in self.hands]

        if current_ranks == ['A', 'A']:
            self.score = 12
            return

        initial_score = 0
        for rank in current_ranks:
            if rank == 'A':
                initial_score += 11
                continue
            initial_score += Card.rank_to_score_except_ace(rank)

        self.score = initial_score

    def update_score(self):
        """Updates player's score attribute after they hits.

        After a player chooses 'hit', they gets a new card. This function
        calculates the latest score after getting the new card and updates
        the player's score attribute.

        Logic of calculating the updated score:

        Case #1: The new card has a rank of 'A'.
        To optimize the total score, first we try to score the new 'A'
        as 11 and adds it to the current score, if the new score exceeds
        21 (bust), then the new 'A' can only be scored as 1, otherwise
        the new 'A' is scored as 11 to maximize the score.

        Case #2: The new card does not have a rank of 'A'.
        Use the static method Card.rank_to_score_except_ace(rank) to
        get the score of the new card's rank, add it to the current
        score and thus get a new score.

        """
        new_card = self.hands[-1]

        if new_card.rank == 'A':
            if self.score + 11 <= 21:
                self.score += 11
                return
            self.score += 1
        else:
            self.score += Card.rank_to_score_except_ace(new_card.rank)


class HumanPlayer(Player):
    """Human player in the game.

    Attributes:
        player_name (str): The name of the player.
        hands (:obj:`list` of :obj:`Card`): The player's hands of cards.
        is_bust (bool): True if the player busts, False otherwise.
        score (int): The player's score.

    """

    def __init__(self, player_number):
        """Constructs an instance of HumanPlayer.

        Args:
            player_number (int): The serial number of the player, starting
                from 1. The serial number is unique among human players.
        """
        self.player_name = "Human Player " + str(player_number)
        self.hands = []
        self.is_bust = False
        self.score = 0

    def get_decision(self):
        """Gets the human player's decision of 'hit' or 'stand' in their turn.

        When it is the human player's turn, this function interactively
        prompts the human player to enter a code to indicate their decision
        (1-hit, 2-stand).

        Returns:
            int: A code of decision, 1 for 'hit', 2 for 'stand'.

        Raises:
            ValueError: If the human player's input is neither 1 nor 2.

        """
        while True:
            try:
                message = self.player_name + " (current score: " + str(self.score) + "): Please choose to hit or " \
                                                                                     "stand: 1-hit, 2-stand\n "
                decision = int(input(message))
                if decision in (1, 2):
                    return decision
                raise ValueError("Invalid input. Please enter 1 or 2.")
            except ValueError as invalid_input_error:
                print(invalid_input_error)
                continue


class ComputerPlayer(Player):
    """ComputerPlayer in the game.

    Attributes:
        player_name (str): The name of the player.
        hands (:obj:`list` of :obj:`Card`): The player's hands of cards.
        is_bust (bool): True if the player busts, False otherwise.
        score (int): The player's score.

    """
    def __init__(self, player_number):
        """Constructs an instance of a ComputerPlayer.

        Args:
            player_number (int): The serial number of the player, starting
                from 1. The serial number is unique among computer players.
        """
        self.player_name = "Computer Player " + str(player_number)
        self.hands = []
        self.is_bust = False
        self.score = 0

    def get_decision(self):
        """Gets the computer player's decision of 'hit' or 'stand' in their turn.

        The computer player randomly choose between 1 and 2 (1-hit, 2-stand).

        Returns:
            int: A code of decision, 1 for 'hit', 2 for 'stand'.

        """
        return random.randint(1, 2)