import random as random

class Card:
  """
  Represents a normal playing card
  """
  # Class attributes  
  suits = ['h', 'd', 'c', 's']
  ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit
  def getRank(self):
    return self.rank
  # Getter method for suit
  def getSuit(self):
    return self.suit

# Inherits from Card
class Deck(Card):
  """
  Represents a deck of normal playing cards
  """
  def __init__(self):
    # self.deck = [None] * 52 # Initialize fixed array size
    self.deck_of_cards = []
    for rank in range(13):
      for suit in range(4):
        self.deck_of_cards.append(Card(rank, suit))
        # self.deck.append(Card (str(rank), suit) )
  def shuffle(self):
    # Shuffle deck
    random.shuffle(self.deck_of_cards)

  def sort(self):
    self.deck_of_cards.sort()

  # Reset deck
  def reset(self):
    self.deck = []
    suits = ['h', 'd', 'c', 's']
    ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    for rank in ranks:
      for suit in suits:
        self.deck.append(Card(rank, suits))
  
  def add_card(self, card):
    self.deck_of_cards.append(card)

  def move_cards(self, hand, num):
    for i in range(num):
      hand.add_card()

  def deal(self):
    return self.deck_of_cards.pop()

  # Burn a card
  def burn(self):
    self.deck_of_cards.pop()

  # Check if deck is empty
  def isEmpty(self):
    return len(self.deck_of_cards) == 0

  def __str__(self):
    ans = [str(card) for card in self.deck_of_cards]
    return '\n'.join(ans)


# Hand inherits from Deck
class Hand(Deck):
  """
  Represents a player's hand of cards
  """
  def __init__(self, name = ''):
    self.name = name
    self.deck_of_cards = []
    self.numPlayers = 6

  def add_card(self, card):
    self.deck_of_cards.append(card)

  def __str__(self): 
      return "Hand is % s, ""b is % s" % (self.deck_of_cards, self.name)

class Frequency(dict):
  def __init__(self, arr = []):
    for i in arr:
      self.count()

  def count(self, item, incr):
    self[item] = self.get(item, 0) + incr

    if self[item] == 0:
      del self[item]
    
