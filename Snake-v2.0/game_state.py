import snake
import game_world
import pygame
import fruit
import random

class Game_State:

    def __init__(self, config):
        #containers etc
        #world

        #ska världen hålla koll på ormen eller ska ormen veta om den hamnar utanför ramen. 
        self.world = game_world.World(config)
        self.world_list = self.world.world
        self.python = snake.Snake(self.world_list, config)

        #etc

        # screen = screen_window # as this should be the same screen as world is written at
        # world = worldobject
        # snake = snake
        # fruit = fruit

    def start(self, screen, font):
        #gameloop
        game_over = False
        clock = pygame.time.Clock()
        fruit_list = []
        key_l = []
        outcome = []

        while not game_over:
            if len(fruit_list) == 0:
                self.place_fruit(self.world_list, self.python, fruit_list)
            
            self.world.render(screen, self.world_list, self.python, fruit_list, font)
        
            for event in pygame.event.get():
                pressed_key = "Not pressed"
            
                if event.type == pygame.locals.QUIT:
                    game_over = True
                elif event.type == pygame.locals.KEYDOWN:
                    pressed_key = event.key
                
                key_l.append(pressed_key)
        
            if len(key_l) == 0:
                key_l.append("Not pressed")

            clock.tick(8)
            self.python.update(key_l.pop(0), self.world_list, fruit_list)

            if not self.python.alive:
                game_over = True

        
        #detta obj håller paus screen?
        return outcome
    
    def place_fruit(self, world, snake, fruit_list):
        """
        Places a fruit on the map by random x and y coord.
        """
        window_min_x = world[0][0][0]
        window_min_y = world[0][0][1]
        window_max_x = world[0][len(world) - 1][0]
        window_max_y = world[len(world) - 1][0][1]
        
        x_coord = random.randrange(window_min_x, window_max_x, 10)
        y_coord = random.randrange(window_min_y, window_max_y, 10)
        fruit_pos = (y_coord, x_coord)
        
        if list(fruit_pos) in snake.body:
            self.place_fruit(self.world_list, snake, fruit_list)
        else:
            fruiit = fruit.Fruit(fruit_pos)
            fruit_list.append(fruiit)

        #def render(self):
            
        #return
