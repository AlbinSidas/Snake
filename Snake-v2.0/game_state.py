import snake
import game_world
import pygame
from fruit import Fruit
import random

class Game_State:

    def __init__(self, config):
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

            """
            Här inväntar spelet en input från en användare
            #TODO
            """
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
                # TODO
                # Om en AI ska kunna träna måste den startas om automatiskt här.
                # Speciellt om en Qlearning ska kunna tränas*** 
                # Isåfall är det att reseta ormen och poängen och starta om spelet? 
                # Se till att modellen försöker maximera poängen och en "död" ger stora
                # minuspoäng

                game_over = True

        
        
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
        fruit_pos = (x_coord, y_coord)
        
        if list(fruit_pos) in snake.body:
            self.place_fruit(self.world_list, snake, fruit_list)
        else:
            fruit_list.append(Fruit(fruit_pos))