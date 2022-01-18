import random
class CounterfactualRegretMinimizer:
  # Subgame

# Implements two-vector resolving that approximates Nash's Equilibrium in current subgame




# Libratus - CMU
# 1. blueprint strategy, 2. nested subgame solving 3. 
  def __init__(self):
    self.v1 = []
    self.v2 = []
    self.left_utility = []

  def propogate_utility(self, state):
    if state.isEnd():
      return state.eval()
      
    ans = 0
    for a in state.actions:
      self.propogate_utility(state.play(a))
      ans += self.sig[state.mySet()][a] * self.left_utility
    return ans
  