from Deck import Deck
# Hand inherits from Deck
class Hand(Deck):
  def __init__(self, name = ''):
    self.deck_of_cards = []
    self.name = name
    self.numPlayers = 6

  def add_card(self, card):
    self.deck_of_cards.append(card)

  def __str__(self): 
      return "Hand is % s, ""b is % s" % (self.deck_of_cards, self.name) 