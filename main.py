import random

class Deck:
  def __init__(self):
    # self.deck = [None] * 52 # Initialize fixed array size
    self.deck = []

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

  # Burn a card
  def burn(self):
    self.deck.pop()

  # Check if deck is empty
  def isEmpty(self):
    return len(self.deck) == 0

class Card(Deck):
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  # Getter method for suit
  def getSuit(self, suit, rank):
    return self.suit
  def getRank(self, suit, rank):
    return self.rank

# Player has a Hand, inherits from Deck
class Player(Deck):
  def __init__(self, name, chips):
    self.name = name
    self.chips = chips
    # self.hand = [None] * 5 # 5 total cards
    self.hand = []
    self.betSize = 0

  ########################
  #### Player Actions ####
  ########################
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

  # Evaluate current hand and power relative to community cards and rankings
  def handPower(self):
    # Evaluate own hand against other cards on board (community cards)
    return

    
class GameState:
    def __init__(self, currAction, betSize, rollingBetSize, remainingPlayerTurns, startingChips):
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
      self.numPlayers = 0
      # Create deck
      self.deck = Deck()
      self.players = []
      self.atFlop = True
      self.community_cards = [] # board
      self.startingChips = startingChips
    """
    Set a bet. 
    Current bet to be matched is betSize.
    rollingBetSize is the total of all bets. Increase rollingBetSize by value of new bet.
    """
    def setBet(self, betSize_):
      g.betSize = betSize_
      g.rollingBetSize += betSize_

    # Asks for a valid input from the user. Returns the action
    def askValidInput(self):
      # Ask for a valid action
      # If someone raised, change actions to Call, Raise, or Fold
      if g.betSize > 0:
        action = input("Choose an action. Call: 'c', Raise: 'b', Fold: 'f'")
      # Else ask for normal input
      else:
        action = input("Choose an action. Check: 'k', Bet: 'b', Fold: 'f' ")

      return action

    # If one turn has finished, reset values and add all bets to pot
    def turnFinished(self):
      if self.remainingPlayerTurns == 0:
        # Add all bets into pot
        self.pot += self.rollingBetSize
        # After everyone calls, global bet size == 0
        self.betSize = 0
        # Reset rollingSum of all bets
        self.rollingBetSize = 0
        print("g.pot at end of all turns: ", self.pot)

    def flop(self):
      if self.remainingPlayerTurns == 0 and self.atFlop:
        self.community_cards.append(self.deck.deal())
        self.community_cards.append(self.deck.deal())
        self.community_cards.append(self.deck.deal())
        self.atFlop = False # set to turn and river
        print(self.community_cards)

    def turn(self):
          self.community_cards.append(self.deck.deal())
          print(self.community_cards)
    def river(self):
          self.community_cards.append(self.deck.deal())
          print(self.community_cards)
      

      
    def setupGame(self):
      self.deck.reset()
      self.deck.shuffle()
      self.numPlayers = int(input("Enter total number of players: "))
      self.startingChips = int(input("Enter starting chip size: "))
      for i in range(self.numPlayers):
        input_player_name = input("Enter name: ")
        # Append new player to player array
        self.players.append(Player(input_player_name, self.startingChips))
        self.players[i].hand.append(self.deck.deal())
        self.players[i].hand.append(self.deck.deal())
        print("Player", i, ":", self.players[i].hand)
    

    def playGame(self):
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
        self.remainingPlayerTurns = self.numPlayers
        while (g.remainingPlayerTurns > 0):
          currPlayer = self.players[currPlayer_i]
          print(currPlayer.name, "'s turn'")

          # Ask for a valid input
          action = g.askValidInput()
          ################################
          ######## Player Actions ########
          ################################
          # Player calls
          if action == 'c':
            # If current player calls, subtract players chips
            currPlayer.chips -= self.betSize
            # Add new bet to total betSize
            self.rollingBetSize += self.betSize
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
            self.setBet(betSize_)
            self.remainingPlayerTurns = self.numPlayers
            print("Current bet to be matched:", self.betSize)
            
          # Player checks, continue to next round
          elif action == 'k':
            currPlayer.check()
        
          # Player folds, muck cards
          elif action == 'f':
            currPlayer.fold()
            continue

          # Change variables needed for for-loop and while-loop
          # Decrement number of turns needed to advance to next community card
          g.remainingPlayerTurns -= 1
          totalTurns += 1
          # print("totalTurns: ", totalTurns)
          currPlayer_i = totalTurns % len(self.players) # Cycle between players using mod
          # print("currPlayer_i: ", currPlayer_i)
          print("g.remainingPlayerTurns", self.remainingPlayerTurns)
          print("g.betSize: ", self.betSize)
          print("g.rollingBetSize: ", self.rollingBetSize)
          ################################
          ######## END OF IF LOOP ########
          ################################

        ################################
        ######## IN WHILE LOOP #########
        ################################
          
        # After all players have taken their turns.
        self.turnFinished()
        # Flop turns three cards.
        self.flop()
        # Turn and river flips one community card.
        self.turn()
        self.river()
        
        
        print("Pot size:", g.pot)


  # Prepare game
# d = Deck()
# d.reset()
# d.shuffle()
# Deal cards to players
# players = [] # Player array to store all total players
# numPlayers = int(input("Enter total number of players: "))
# numPlayers = 6
# startingChips = int(input("Enter starting chip size: "))
# startingChips = 1000

# for i in range(numPlayers):
#   input_player_name = input("Enter name: ")
# # Append new player to player array
#   players.append(Player(input_player_name, startingChips))
#   players[i].hand.append(d.deal())
#   players[i].hand.append(d.deal())
#   print("Player", i, ":", players[i].hand)


  # def startGame():
# g = GameState(0, 0, 0, numPlayers)
g = GameState(0, 0, 0, 6, 1000)
g.setupGame()
g.playGame()