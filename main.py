import pygame as pg
import sys
from settings import *
#from next_level import *
from map1 import *
#my code to import maps 2 & 3
from map2 import *
#from map3 import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *

levels= ( #store your levels in a convenient structure
    Map1(map),
    Map2(map),
    #Map3(map),
)

#next_level.current_level_index = 0

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        pg.event.set_grab(True)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)
        #self.current_level_index()
        self.new_game()


    #def current_level_index(self):
        #if next_level.current_level_index == 0:
            #self.new_game()
        #if next_level.current_level_index == 1:
            #self.new_game()
        #current_level_index = 0 # The level state, initalized with the index of the first level
        #self.object_handler.check_win() == False
        #while True:
            #level = levels[current_level_index] # use your state to get the level instead of naming it directly
            #level.get_map()# whatever you need to do to update your level logic, move things etc
            #if self.object_handler.check_win():
                #current_level_index += 1
                #self.new_game()

    #def current_level_index(self):
        #if ObjectHandler.next_level.self.current_level_index == 0:
            #self.map = Map1(self)
            #self.new_game()
        #elif ObjectHandler.next_level.self.current_level_index == 1:
            #self.map = Map2(self)
            #self.new_game()
        

    def new_game(self):
        self.map = Map1(self)
        #elif next_level.current_level_index == 1:
            #self.map = Map2(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)
        pg.mixer.music.play(-1)
        #self.map = Map2(self)
        #self.player = Player(self)
        #self.object_renderer = ObjectRenderer(self)
        #self.raycasting = RayCasting(self)
        #self.object_handler = ObjectHandler(self)
        #self.weapon = Weapon(self)
        #self.sound = Sound(self)
        #self.pathfinding = PathFinding(self)
        #pg.mixer.music.play(-1)

    #my code for next level script
    
         
    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')   

    def draw(self):
        # self.screen.fill('black')
        self.object_renderer.draw()
        self.weapon.draw()
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()



if __name__ == '__main__':
    game = Game()
    game.run()
