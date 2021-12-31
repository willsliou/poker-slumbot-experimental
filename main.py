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
    print(currPlayer.name, "folds.")

  def bet(self, betSize):
    # GameState.betSize = betSize
    self.chips = self.chips - betSize
    print(self.name, " bets $", betSize, "Chips left $", self.chips)

  def check(self):
    print(currPlayer.name, 'checks.')
  


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
    def __init__(self, currAction, betSize, remainingPlayerTurns):
      self.currAction = currAction
      self.pot = 0
      self.betSize = betSize
      self.remainingPlayerTurns = remainingPlayerTurns
    # def setBet(size):
      
      
    
#   def playGame():
    
    


turnCounter = 0 # Track at flop or not

  # Prepare game
d = Dealer()
d.reset()
d.shuffle()
# Deal cards to players
players = [] # Player array to store all total players
# numPlayers = int(input("Enter total number of players: "))
numPlayers = 3
# startingChips = int(input("Enter starting chip size: "))
startingChips = 1000

for i in range(numPlayers):
  input_player_name = input("Enter name: ")
# Append new player to player array
  players.append(Player(input_player_name, startingChips))
  players[i].hand.append(d.deal())
  players[i].hand.append(d.deal())
  print("Player", i, ":", players[i].hand)


  # def startGame():
g = GameState(0, 0, numPlayers)
# p1 = Player('Joe Biden', 1000)
# p2 = Player('Trump', 1000)
# players.append(p1)
# players.append(p2)

# p1.hand.append(d.deal())
# p1.hand.append(d.deal())
# p2.hand.append(d.deal())
# p2.hand.append(d.deal())
# print("Player 1: ", p1.hand)
# print("Player 2: ", p2.hand)

# action = input("Choose an action. Check: 'k', Call: 'c', Bet: 'b', Fold: 'f' ")

# Simulate full round with 3 turns. (Preflop, Flop, Turn, River)
currPlayer_i = 0
totalTurns = 0
for i in range(0, 3):
  # j represents the current player, totalTurns represents total turns
  g.remainingPlayerTurns = numPlayers
  while (g.remainingPlayerTurns > 0):
    currPlayer = players[currPlayer_i]
    print(currPlayer.name, "'s turn'")
    # If someone raised, change actions to Call, Raise, or Fold
    if g.betSize > 0:
      action = input("Choose an action. Call: 'c', Raise: 'b', Fold: 'f'")
    # Else ask for normal input
    else:
      action = input("Choose an action. Check: 'k', Bet: 'b', Fold: 'f' ")

      
    # Player calls
    if action == 'c':
      # If current player calls, subtract players chips
      currPlayer.chips -= g.betSize
      # Double individual player's bets. Add bet size to total pot.
      g.pot += (g.betSize*2)
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
      g.remainingPlayerTurns = numPlayers
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

    g.remainingPlayerTurns -= 1
    totalTurns += 1
    print("totalTurns: ", totalTurns)
    currPlayer_i = totalTurns % len(players) # Cycle between players using mod
    print("currPlayer_i: ", currPlayer_i)
    print("g.remainingPlayerTurns", g.remainingPlayerTurns)
    print("g.betSize: ", g.betSize)

  if g.remainingPlayerTurns == 0:
    # After everyone calls, global bet size == 0
    g.betSize = 0
  # Flop turns three cards.
  if g.remainingPlayerTurns == 0 and turnCounter == 0:
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
    