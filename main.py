import random

class Dealer:
  def __init__(self):
    # self.deck = [None] * 52 # Initialize fixed array size
    self.deck = []
    self.community_cards = []

  # Shuffle deck
  def shuffle(self):
    random.shuffle(self.deck)

  # Reset deck
  def reset(self):
    self.deck = []
    suits = ['h', 'd', 'c', 's']
    ranks = ['A', 2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K']

    for rank in ranks:
      for suit in suits:
        self.deck.append(str(rank) + suit)

  # Deal next card

  # def dealCards1(self):
  #   Player.hand.append(self.deck.pop())
  #   Player.hand.append(self.deck.pop())
    
  def deal(self):
    return self.deck.pop()

  # Check if deck is empty
  def isEmpty(self):
    return len(self.deck) == 0

class Player:
  def __init__(self, name, chips):
    self.name = name
    self.chips = chips
    # self.hand = [None] * 5 # 5 total cards
    self.hand = []

  def fold(self):
    print("Folding")

  def bet(self, betSize):
    # GameState.betSize = betSize
    self.chips = self.chips - betSize
    print(self.name, " bets $", betSize, "Chips left $", self.chips)

  def check(self):
    print("Check")
  


class Card:
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  # Getter method for suit
  def getSuit(self, suit, rank):
    return self.suit
  def getRank(self, suit, rank):
    return self.rank

    
class GameState:
    def __init__(self, currAction, betSize):
      self.currAction = currAction
      self.pot = 0
      self.betSize = betSize
    # def setBet(size):
      
      
    
#   def playGame():
    
    

# def startGame():
  # Prepare game
d = Dealer()
d.reset()
d.shuffle()

g = GameState(0, 0)
players = [] # Player array to store all total players
turnCounter = 0
# Deal cards to players
# numPlayers = input("Enter total number of players: ")
# startingChips = input("Enter starting chip size: ")

# for i in range(numPlayers):
#   input_player_name =  input("Enter name: ")
# # Append new player to player array
#   players.append(Player(input_player_name, startingChips))
p1 = Player('Joe Biden', 1000)
p2 = Player('Trump', 1000)
players.append(p1)
players.append(p2)

p1.hand.append(d.deal())
p1.hand.append(d.deal())
p2.hand.append(d.deal())
p2.hand.append(d.deal())
print("Player 1: ", p1.hand)
print("Player 2: ", p2.hand)

# action = input("Choose an action. Check: 'k', Call: 'c', Bet: 'b', Fold: 'f' ")

# Simulate full round with 3 turns. (Preflop, Flop, Turn, River)
for i in range(0, 3):
  # while g.betSize > 0:
  # j represents the current player, totalTurns represents total turns
  totalTurns = 0
  currPlayer_i = 0
  while (totalTurns < len(players) or g.betSize > 0):
    currPlayer = players[currPlayer_i]
    # If someone raised, change actions to Call, Raise, or Fold
    if g.betSize > 0:
      action = input("Choose an action. Call: 'c', Raise: 'b', Fold: 'f'")
    # Else ask for normal input
    else:
      action = input("Choose an action. Check: 'k', Bet: 'b', Fold: 'f' ")
  
  
  
    
    # Player calls, reduce global betSize to 0
    if action == 'c':
      # If current player calls, subtract players chips
      currPlayer.chips -= g.betSize
      # Double individual player's bets. Add bet size to total pot.
      g.pot += (g.betSize*2)
      # After the call, bets are 0
      g.betSize = 0
      print(currPlayer.name, "calls. Total chips: $", currPlayer.chips)
      
    # Player bets, ask for input. Call Player.bet() to reduce individual player chip size. Increase global bet size.
    elif action == 'b':
      betSize_ = int(input("Input your bet size: "))

      ########### Betting options ###########
      # Minimum Bet
      
      
      # Half Pot

      # Full Pot
      # if betSize_
      # Shove all in

      
      currPlayer.bet(betSize_)
      g.betSize += betSize_
      print("Global betsize:", g.betSize)
    
    # Player checks, continue to next round
    elif action == 'k':
      currPlayer.check()
      # print("Player checks")
  
    # Player folds, muck cards
    elif action == 'f':
      currPlayer.fold()
      raise StopIteration

    totalTurns += 1
    currPlayer_i = totalTurns % len(players) # Cycle between players using mod

  # Flop turns three cards.
  if turnCounter == 0:
    d.community_cards.append(d.deal())
    d.community_cards.append(d.deal())
    d.community_cards.append(d.deal())
    print(d.community_cards)
  # Turn and river turn one card.
  else:
    d.community_cards.append(d.deal())
    print(d.community_cards)
  turnCounter += 1
  
  print("Pot size:", g.pot)



# # Flop
# d.community_cards.append(d.deal())
# d.community_cards.append(d.deal())
# d.community_cards.append(d.deal())
# print("Flop: ", d.community_cards)
# # Turn
# d.community_cards.append(d.deal())
# print("Turn: ", d.community_cards)
# # River
# d.community_cards.append(d.deal())
# print("River: ", d.community_cards)

# startGame()
    