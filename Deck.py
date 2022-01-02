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
      hand.add_card(self.deck_of_cards.pop())

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
  "Frequency map of each item to a key value pair"
  def __init__(self, arr = []):
    for i in arr:
      self.count()

  def count(self, item, incr):
    self[item] = self.get(item, 0) + incr

    if self[item] == 0:
      del self[item]

class FiveCardPokerHand(Hand):

  def __init__(self):
    self.ranks = ''
    self.suits = ''
    self.sorted = []


  
  self.ranks = Frequency()
  self.suits = Frequency()

  for c in self.deck_of_cards:
    self.suits.count(c.suit)
    self.ranks.count(c.rank)

  self.sorted = self.ranks.values()
  self.sorted.sort(reverse=True)


  def has_highcard(self):
    return len(self.deck_of_cards)

  

# Player has a Hand, inherits from GameState
class Player(Hand):
  def __init__(self, name, chips):
    self.name = name
    self.chips = chips
    # self.hand = [None] * 5 # 5 total cards
    # self.hand = []
    self.betSize = 0
    self.isFolded = False

  ########################
  #### Player Actions ####
  ########################
  def fold(self):
    self.isFolded = True
    print(self.name, "folds.")

  def bet(self, betSize):
    # GameState.betSize = betSize
    self.chips = self.chips - betSize
    self.betSize = betSize
    print(self.name, " bets $", betSize, "Total chips: $", self.chips)

  def check(self):
    print(self.name, 'checks.', "Total chips: $", self.chips)

  def call(self):
    print(self.name, "calls. Total chips: $", self.chips)

    
    
