import random
import itertools
from Card import Card
from Deck import Deck
from Hand import Hand
from Player import Player
from GameState import GameState


    
  # def startGame():
# g = GameState(0, 0, 0, numPlayers)
numGames = 2
# for i in range(numGames):
  # print("######## New Game: ########", i)
g = GameState(0, 0, 0, 6, 1000)
g.setupGame()
g.evalProbability()
g.playGame()

