#from next_level import *
from map1 import *
from map2 import *
from sprite_object import *
from npc import *
from random import choices, randrange

#This is a modified version of the original object_handler.py that disables the level check_win() loop

levels= ( #store your levels in a convenient structure
    Map1(map),
    Map2(map),
    #Map3(map),
)

#current_level_index = 0

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        #self.current_level_index = 0 # The level state, initalized with the index of the first level
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        # spawn npc
        self.enemies = 20  # npc count
        self.npc_types = [SoldierNPC, CacoDemonNPC, CyberDemonNPC]
        self.weights = [70, 20, 10]
        self.restricted_area = {(i, j) for i in range(10) for j in range(10)}
        self.spawn_npc()

        #add_npc(SoldierNPC(game, pos=(11.0, 19.0)))
        #add_npc(SoldierNPC(game, pos=(11.5, 4.5)))
        #add_npc(SoldierNPC(game, pos=(13.5, 6.5)))
        #add_npc(SoldierNPC(game, pos=(2.0, 20.0)))
        #add_npc(SoldierNPC(game, pos=(4.0, 29.0)))
        #add_npc(CacoDemonNPC(game, pos=(5.5, 14.5)))
        #add_npc(CacoDemonNPC(game, pos=(5.5, 16.5)))
        #add_npc(CyberDemonNPC(game, pos=(14.5, 25.5)))

        # sprite map
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(6.5, 1.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(9.5, 19.5)))
        add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(13.5, 19.5)))
        #add_sprite(AnimatedSprite(game, pos=(5.5, 3.25)))
        #add_sprite(AnimatedSprite(game, pos=(5.5, 4.75)))
        #add_sprite(AnimatedSprite(game, pos=(7.5, 2.5)))
        #add_sprite(AnimatedSprite(game, pos=(7.5, 5.5)))
        #add_sprite(AnimatedSprite(game, pos=(14.5, 1.5)))
        #add_sprite(AnimatedSprite(game, pos=(14.5, 4.5)))
        #add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 5.5)))
        #add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 7.5)))
        #add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(12.5, 7.5)))
        #add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(9.5, 7.5)))
        #add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 12.5)))
        #add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(9.5, 20.5)))
        #add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(10.5, 20.5)))
        #add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(3.5, 14.5)))
        #add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(3.5, 18.5)))
        #add_sprite(AnimatedSprite(game, pos=(14.5, 24.5)))
        #add_sprite(AnimatedSprite(game, pos=(14.5, 30.5)))
        #add_sprite(AnimatedSprite(game, pos=(1.5, 30.5)))
        #add_sprite(AnimatedSprite(game, pos=(1.5, 24.5)))


        ##note. this is useful code for programming future BOOM levels.
        
            #npc map

    def spawn_npc(self):
        for i in range(self.enemies):
                npc = choices(self.npc_types, self.weights)[0]
                pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
                while (pos in self.game.map.world_map) or (pos in self.restricted_area):
                    pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
                self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5)))

    #def next_level(self):
        #current_level_index = 0
        #if self.check_win() is True:
            #current_level_index += 1
            #self.game.new_game()

    #def next_level(self):
        #current_level_index = 0
    #self.object_handler.check_win() == False
        #if len(self.npc_positions):
        #while True:
            #level = levels[self.current_level_index] # use your state to get the level instead of naming it directly
            #level.get_map()# whatever you need to do to update your level logic, move things etc
        #if self.object_handler.check_win() == True:
        #if not len(self.npc_positions):
            #current_level_index += 1
            #self.game.new_game()

    def check_win(self):
        current_level_index = 0
        if not len(self.npc_positions):
            if current_level_index is 0:
                current_level_index += 1
                self.game.object_renderer.win()
                pg.display.flip()
                pg.time.delay(1500)
                self.game.level_one()
            elif current_level_index is 1:
                current_level_index += 1
                self.game.object_renderer.win()
                pg.display.flip()
                pg.time.delay(1500)
                self.game.level_two()
            elif current_level_index is 2:
                current_level_index += 1
                self.game.object_renderer.win()
                pg.display.flip()
                pg.time.delay(1500)
                self.game.level_three()

            #self.game.current_level_index()
            #self.next_level()
            #mycode
            #self.game.next_level()
            #level = levels(current_level_index)
            #my code for next level script

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        #self.next_level()
        self.check_win()
        #pg.time.delay(3000)
        #self.game.next_level()

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

   





