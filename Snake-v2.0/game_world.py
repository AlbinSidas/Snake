import pygame
import pygame.locals
import config

class World:

    def __init__(self, config):

        screen_width, screen_height = config.settings["Screensize"].split("x")
        self.screen_width = int(screen_width)
        self.screen_height = int(screen_height)

        self.tile_size = int(config.settings["Tilesize"])
        self.refreshrate = int(config.settings["Snake speed"])
        self.map_size = int(config.settings["Boardsize"])

        self.world = self.create_map()
        
    def create_map(self):
        """
        Returns a list with lists of tuples which symbolize every tile
        on the board. 
        """
        map_pos_x = self.screen_width / 4
        map_pos_y = self.screen_height / 8
        world = []
        
        for lines in range(0, self.map_size):
            line = []

            for tiles in range(0, self.map_size):
                tile = (int(tiles * self.tile_size + map_pos_x),
                        int(lines * self.tile_size + map_pos_y))
                line.append(tile)

            world.append(line)

        return world

    def render(self, screen, world, snake, fruit_list, font):
        """
        Handles all the positioning and updating for each frame. 
        """
        world_side_length = self.tile_size * len(self.world)
        frame_pos_x = self.world[0][0][0]
        frame_pos_y = self.world[0][0][1]
        score_text = font.render("Your score: {}".format(snake.score),
                                 False, (0,0,0))

        screen.fill((255, 255, 255))
        screen.blit(score_text, (self.screen_width / 4 , self.screen_height / 1.7))

        pygame.draw.rect(screen, 0, (frame_pos_x, frame_pos_y,
                                     world_side_length, world_side_length), 1)

        
        self.drawer(screen, world, snake, fruit_list)
        
        pygame.display.update()
        pygame.display.flip()

    def drawer(self, screen, world, snake, fruit_list):
        """
        Handles all drawing within the world rectangle. 
        """

        for lines in world:
            for tiles in lines:
                for body in snake.body:

                    if tuple(body) == tiles:
                        #Checks where the head of the snake is on the board.
                        pygame.draw.rect(screen, 0,(body[0], body[1],
                                                    self.tile_size, self.tile_size))
                
                
                if fruit_list[0].pos == tiles:
                    pygame.draw.rect(screen, 155,
                                    (tiles[0], tiles[1], self.tile_size, self.tile_size))
                #Draws every rectangle in the playingfield
                #pygame.draw.rect(screen, 0,(tiles[0], tiles[1],
                #                          tile_width, tile_height), 1)
                    
        
         



if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((700, 600))
    font = pygame.font.SysFont('Comic Sans MS', 30)
    c = config.Config("config.txt")
    w = World(c)
    
    #w.render
