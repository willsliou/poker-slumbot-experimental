import random
class CounterfactualRegretMinimizer:
  # Subgame

# Implements two-vector resolving that approximates Nash's Equilibrium in current subgame




# Libratus - CMU
# 1. blueprint strategy, 2. nested subgame solving 3. 
  def __init__(self):
    self.v1 = []
    self.v2 = []
    self.v3 = []

def propogate_utility(self, state):
  if state.isEnd():
    return state.eval()
    

def utility(self, state):
  if state.isEnd():
    return 0

  ans = 0
  for a in state.actions:
    left_node = self.