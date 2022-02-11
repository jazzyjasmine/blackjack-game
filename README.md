# Blackjack Game

Note that there is no betting. Instead, at the end of the round, the player or dealer with the highest score is declared the winner.  

For each round:
- The dealer shuffles the deck.
- The dealer gives 1 card face-up to all players; and 1 card face-up to themself.
- The dealer gives 1 card face-up to all players; and 1 card face-down to themself.
- For each player’s turn:
    - The player decides to “hit” (receive one more card from dealer) or “stand” (receive no more cards and immediately end their turn). If the player hits and their new score is >21, then they “bust”, meaning that their turn immediately ends and they immediately lose.
    - Repeat until the player’s turn ends, either because they stand or bust.
- For the dealer’s turn:
    - The dealer reveals their face-down card.
    - If the dealer’s score is ≥17, they must stand.
    - If the dealer’s score is <17, they must continue to deal cards to themself until their score is ≥17. If their score ever becomes >21, they bust and immediately lose.
- Declare the winner of this round. The winner is the player or dealer with the highest score.
- Prompt the human players if they want another round.