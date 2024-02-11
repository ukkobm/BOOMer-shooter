import pygame as pg
from object_handler import *
from map1 import *
from map2 import *
#from map3 import *

levels= ( #store your levels in a convenient structure
    Map1(map),
    Map2(map),
    #Map3(map),
)


class next_level:
  def __init__(self, game):
    self.game = game
    self.current_level_index = 0 # The level state, initalized with the index of the first level

  def current_level_index(self):
    #self.current_level_index = 0
    #self.object_handler.check_win() == False
    if len(self.npc_positions):
      level = levels[self.current_level_index] # use your state to get the level instead of naming it directly
      level.get_map()# whatever you need to do to update your level logic, move things etc
      #if self.object_handler.check_win() == True:
      if not len(self.npc_positions):
        self.current_level_index += 1
        self.game.new_game()