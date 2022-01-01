import random

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

# Player has a Hand, inherits from GameState
class Player(Hand):
  def __init__(self, name, chips):
    self.name = name
    self.chips = chips
    # self.hand = [None] * 5 # 5 total cards
    self.hand = []
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
      self.d = Deck()
      self.players = []
      self.players_copy = []
      self.roundNumber = 0 # Tracks if we are at the flop, turn, or river
      self.community_cards = [] # board
      self.startingChips = startingChips
      self.isEnd = False
      self.currPlayer_i=0
      self.playersLeft = 0
    """
    Set a bet. 
    Current bet to be matched is betSize.
    rollingBetSize is the total of all bets. Increase rollingBetSize by value of new bet.
    """
    def setBet(self, betSize_):
      self.betSize = betSize_
      self.rollingBetSize += betSize_

    # Asks for a valid input from the user. Returns the action
    def askValidInput(self):
      # Ask for a valid action
      # If someone raised, change actions to Call, Raise, or Fold
      if self.betSize > 0:
        action = input("Choose an action. Call: 'c', Raise: 'b', Fold: 'f'")
      # Else ask for normal input
      else:
        action = input("Choose an action. Check: 'k', Bet: 'b', Fold: 'f' ")

      return action

    def strengthOfHand(self):
      """
      >>> g.players[0].hand  
      ['4c', '10d']
      """
      # Ace == 1, Spade == 0, Diamond == 1, Heart == 2, Club == 3
      aces = {'As': 10, 'Ad': 11, 'Ah':12, 'Ac': 13}
      kings = {'Ks': 130, 'Kd': 131, 'Kh':132, 'Kc': 133}
      queens = {'Qs': 120, 'Qd': 121, 'Qh':122, 'Qc': 123}
      jacks = {'Js': 110, 'Jd': 111, 'Jh':112, 'Jc': 113}
      tens = {'10s': 100, '10d': 101, '10h':102, '10c': 103}
      
      for p in self.players:
        # Check if hand has strong pairs
        if p.hand[0] in aces and p.hand[1] in aces:
          print(p.name, "Pocket Aces. Rockets!")
        if p.hand[0] in kings and p.hand[1] in kings:
          print(p.name, "Pocket Kings. Cowboys!")
        if p.hand[0] in queens and p.hand[1] in queens:
          print(p.name, "Pocket Queens. Ladies!")
        if p.hand[0] in jacks and p.hand[1] in jacks:
          print(p.name, "Pocket Jacks. Hooks!")
        if p.hand[0] in tens and p.hand[1] in tens:
          print(p.name, "Pocket Tens. Dimes!")

        if p.hand[0] in aces and p.hand[1] in kings or p.hand[1] in aces and p.hand[0] in kings:
          print(p.name, "Ace King offsuit. Big Slick!")
        if p.hand[0] in aces and p.hand[1] in queens or p.hand[1] in aces and p.hand[0] in queens:
          print(p.name, "Ace Queen offsuit. Big Chick!")
        if p.hand[0] in aces and p.hand[1] in jacks or p.hand[1] in aces and p.hand[0] in jacks:
          print(p.name, "Ace Jack offsuit")

        
    # def evaluateWinner(self):
      # if 
            
        # Check hand against board for pairs
          
    
    ##################################
    #### INDIVIDUAL TURN SETTINGS ####
    ##################################
    # If one turn has finished, reset values and add all bets to pot
    def endTurnAddPot(self):
      # Add all bets into pot
      self.pot += self.rollingBetSize
      
    def endTurnReset(self):
      # If all players have finished their turn)
      if self.remainingPlayerTurns == 0:
        # Add all bets into pot
        self.endTurnAddPot()
        # After everyone calls, global bet size == 0
        self.betSize = 0
        # Reset rollingSum of all bets
        self.rollingBetSize = 0
        # Move from preflop to flop, increment round counter by 1
        # self.roundNumber += 1

    def flop(self):
      # If all players have finished their turn and we are at the flop)
      print("flop")
      print(self.roundNumber)
      if self.remainingPlayerTurns == 0 and self.roundNumber == 1:
        self.community_cards.append(self.d.deal())
        self.community_cards.append(self.d.deal())
        self.community_cards.append(self.d.deal())
        self.atFlop = False # set to turn and river
        print(self.community_cards)
    def turn(self):
      # If all players have finished their turn and we are at the turn)
      if self.remainingPlayerTurns == 0 and self.roundNumber == 2:
          self.community_cards.append(self.d.deal())
          print(self.community_cards)
    def river(self):
      # If all players have finished their turn and we are at the river)
      if self.remainingPlayerTurns == 0 and self.roundNumber == 3:
          self.community_cards.append(self.d.deal())
          print(self.community_cards)
      

      
    # def setupGame(self):
    #   self.d.reset()
    #   self.d.shuffle()
    #   self.numPlayers = int(input("Enter total number of players: "))
    #   self.startingChips = int(input("Enter starting chip size: "))
    #   for i in range(self.numPlayers):
    #     input_player_name = input("Enter name: ")
    #     # Append new player to player array
    #     self.players.append(Player(input_player_name, self.startingChips))
    #     self.players[i].hand.append(self.d.deal())
    #     self.players[i].hand.append(self.d.deal())
    #     print("Player", i, ":", self.players[i].hand)

#  USING HAND CLASS
#   def deal_initial(self, num_cards = 52):
    # for i in range(self.numPlayers):
    #   for j in range(0, 2):
    #     if self.isEmpty(): break

    #     player_name_input = input("Enter name: ")
    #     Player(player_name_input, 1000)
        
    #     hand.add_card(self.deck_of_cards.pop())
    ########################################
    #### Temporary debugging setup game ####
    ########################################

    
        
    def setupGame(self):
      # self.d.reset()
      self.d.shuffle()
      self.numPlayers = 4
      self.startingChips = 1000

      # Append new player to player array
      self.players.append(Player(0, self.startingChips))
      self.players[0].hand.append(self.d.deal())
      self.players[0].hand.append(self.d.deal())
      print("Player 0", ":", self.players[0].hand)

      self.players.append(Player(1, self.startingChips))
      self.players[1].hand.append(self.d.deal())
      self.players[1].hand.append(self.d.deal())
      print("Player 1", ":", self.players[1].hand)

      self.players.append(Player(2, self.startingChips))
      self.players[2].hand.append(self.d.deal())
      self.players[2].hand.append(self.d.deal())
      print("Player 2", ":", self.players[2].hand)
      
      self.players.append(Player(3, self.startingChips))
      self.players[3].hand.append(self.d.deal())
      self.players[3].hand.append(self.d.deal())
      print("Player 3", ":", self.players[3].hand)
      

    def playGame(self):
      """
      Simulates full round with 3 turns. (Preflop, Flop, Turn, River)
      For three rounds, if there are remaining turns, take each player's action.
      If player calls, subtract current player's chipsize with bet size.
        
      """
      self.currPlayer_i = 0
      # totalTurns = 0
      self.playersLeft = len(self.players) # Players that have not folded
      # 3 total rounds
      # for i in range(0, 3):
      i=0
      # playersOut = 0
      # while we play less than 3 rounds and more than 1 player is in the game (no folded)
      while (i < 3 and self.playersLeft > 1 and not self.isEnd):
        self.strengthOfHand()
        
        # j represents the current player, totalTurns represents total turns
        self.remainingPlayerTurns = self.numPlayers
        # while players still have turns to play and more than 1 player is in the game (not folded)
        while (self.remainingPlayerTurns > 0 and self.playersLeft > 1 and not self.isEnd):          
          currPlayer = self.players[self.currPlayer_i % len(self.players)] # Cycles through players

          # If current player has not folded, ask for input
          if not currPlayer.isFolded:
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
              self.remainingPlayerTurns = len(self.players) # Reset number of rounds from starting position
              print("Current bet to be matched:", self.betSize)
              
            # Player checks, continue to next round
            elif action == 'k':
              currPlayer.check()
          
            # Player folds, muck cards
            elif action == 'f':
              currPlayer.fold()
              self.playersLeft -= 1
  
              if (self.playersLeft == 1):
                # Update original self.players array with new winner and total chips
                for p in self.players:
                  if p.isFolded == False:
                    self.endTurnAddPot() # Add all bets into pot
                    p.chips = g.pot
                    print("Updating ", p.name, "'s chips to$", g.pot)
                self.isEnd = True
                print("All players have folded.")
                break
  
            # playersOut = len(self.players) - playersLeft
          self.remainingPlayerTurns -= 1
          print("self.remainingPlayerTurns: ", self.remainingPlayerTurns)
          self.currPlayer_i+=1
            # totalTurns += 1

            ################################
            ######## END OF IF LOOP ########
            ################################

        ################################
        ######## IN WHILE LOOP #########
        ################################

        # evaluateWinner()
        self.roundNumber+=1 # Finished 1 round. Move onto flop 

        if not self.isEnd:
          # After all players have taken their turns.
          self.endTurnReset()
          # Flop turns three cards.
          # print("flop")
          self.flop()
          self.turn()
          self.river()
          i+=1



    
  # def startGame():
# g = GameState(0, 0, 0, numPlayers)
for i in range(2):
  print("######## New Game: ########", i)
  g = GameState(0, 0, 0, 6, 1000)
  g.setupGame()
  g.playGame()

