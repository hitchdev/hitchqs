Glider:
  given:
    setup: |
      from game import Game
      from state import State
    state: |
      oo.
      o.o
      o..
  steps:
  - run:
      code: |
        my_game = Game(State(state, x = 2, y = 3, width = 10, height = 10))
        my_game.step(2)
        print(my_game.display())
      will output: |-
        . . . . . . . . . .                                                                                                                                            
         . . . . . . . . . .                                                                                                                                            
         . o o o . . . . . .                                                                                                                                            
         . o . . . . . . . .                                                                                                                                            
         . . o . . . . . . .                                                                                                                                            
         . . . . . . . . . .                                                                                                                                            
         . . . . . . . . . .                                                                                                                                            
         . . . . . . . . . .                                                                                                                                            
         . . . . . . . . . .                                                                                                                                            
         . . . . . . . . . .
