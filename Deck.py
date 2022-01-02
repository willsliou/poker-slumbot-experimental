import random as random
from Card import Card

# Inherits from Card
class Deck(Card):
  """
  Represents a deck of cards
  """
  def __init__(self):
    # self.deck = [None] * 52 # Initialize fixed array size
    self.deck_of_cards = []
    for rank in Card.ranks:
      for suit in Card.suits:
        self.deck_of_cards.append(str(rank) + suit)
        # self.deck.append(Card (str(rank), suit) )
  # Shuffle deck
  def shuffle(self):
    random.shuffle(self.deck_of_cards)

  # Reset deck
  # def reset(self):
  #   self.deck = []
  #   suits = ['h', 'd', 'c', 's']
  #   ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

  #   for rank in ranks:
  #     for suit in suits:
  #       self.deck.append(str(rank) + suit)
    
  def deal(self):
    return self.deck_of_cards.pop()

  # Burn a card
  def burn(self):
    self.deck_of_cards.pop()

  # Check if deck is empty
  def isEmpty(self):
    return len(self.deck_of_cards) == 0