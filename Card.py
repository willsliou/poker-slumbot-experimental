class Card:
  suits = ['h', 'd', 'c', 's']
  ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
  # Getter method for suit
  def getSuit(self, suit, rank):
    return self.suit
  def getRank(self, suit, rank):
    return self.rank