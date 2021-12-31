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
    ranks = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    for rank in ranks:
      for suit in suits:
        self.deck.append(str(rank) + suit)
    
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
    self.betSize = 0

  def fold(self):
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
    def __init__(self, currAction, betSize, rollingBetSize, remainingPlayerTurns):
      """
      betSize = current bet on the table
      rollingBetSize = total of all bets during a single turn
      remainingPlayerTurns = Tracks remaining number of turns after a player has bet
      """
      self.currAction = currAction
      self.pot = 0
      self.betSize = betSize
      self.rollingBetSize = rollingBetSize
      self.remainingPlayerTurns = remainingPlayerTurns

    """
    Set a bet. 
    Current bet to be matched is betSize.
    rollingBetSize is the total of all bets. Increase rollingBetSize by value of new bet.
    """
    def setBet(self, betSize_):
      g.betSize = betSize_
      g.rollingBetSize += betSize_
      
    
#   def playGame():
    
    


turnCounter = 0 # Track at flop or not

  # Prepare game
d = Dealer()
d.reset()
d.shuffle()
# Deal cards to players
players = [] # Player array to store all total players
# numPlayers = int(input("Enter total number of players: "))
numPlayers = 6
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
g = GameState(0, 0, 0, numPlayers)

"""
Simulates full round with 3 turns. (Preflop, Flop, Turn, River)
For three rounds, if there are remaining turns, take each player's action.
If player calls, subtract current player's chipsize with bet size.

"""
currPlayer_i = 0
totalTurns = 0
# 3 total rounds
for i in range(0, 3):
  # j represents the current player, totalTurns represents total turns
  g.remainingPlayerTurns = numPlayers
  while (g.remainingPlayerTurns > 0):
    currPlayer = players[currPlayer_i]
    print(currPlayer.name, "'s turn'")
    
    # Ask for a valid action
    # If someone raised, change actions to Call, Raise, or Fold
    if g.betSize > 0:
      action = input("Choose an action. Call: 'c', Raise: 'b', Fold: 'f'")
    # Else ask for normal input
    else:
      action = input("Choose an action. Check: 'k', Bet: 'b', Fold: 'f' ")

    ################################
    ######## Player Actions ########
    ################################
    # Player calls
    if action == 'c':
      # If current player calls, subtract players chips
      currPlayer.chips -= g.betSize
      # Add new bet to total betSize
      g.rollingBetSize += g.betSize
      currPlayer.call()
      
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
      g.setBet(betSize_)
      g.remainingPlayerTurns = numPlayers
      print("Current bet to be matched:", g.betSize)
    
    # Player checks, continue to next round
    elif action == 'k':
      currPlayer.check()
  
    # Player folds, muck cards
    elif action == 'f':
      currPlayer.fold()
      continue

    g.remainingPlayerTurns -= 1
    totalTurns += 1
    # print("totalTurns: ", totalTurns)
    currPlayer_i = totalTurns % len(players) # Cycle between players using mod
    # print("currPlayer_i: ", currPlayer_i)
    print("g.remainingPlayerTurns", g.remainingPlayerTurns)
    print("g.betSize: ", g.betSize)
    print("g.rollingBetSize: ", g.rollingBetSize)

  # After all players have taken their turns.
  if g.remainingPlayerTurns == 0:
    # Add all bets into pot
    g.pot += g.rollingBetSize
    # After everyone calls, global bet size == 0
    g.betSize = 0
    # Reset rollingSum of all bets
    g.rollingBetSize = 0
    print("g.pot at end of all turns: ", g.pot)
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
    