import pygame
import pygame.locals
import random

def create_map(screen_w, screen_h, height = 20, width = 20):
    move_map_top = screen_h / 8
    move_map_right = screen_w / 4
    world = []
    for lines in range(0,height):
        line = []

        for tiles in range(0, width):
            tile = (int(lines * 10 + move_map_right),
                    int(tiles * 10 + move_map_top))
            line.append(tile)

        world.append(line)

    #print(world) Prints the world coordinates.
    return world

def render(screen, world, snake, fruit_list, font):
    """
    Sets the tile size and mainly 
    renders the board.
    """ 
    
    tile_height = 10
    tile_width = 10
    
    x_max = find_window_x_coord(world)
    y_max = find_window_y_coord(world)
    
    #These two variables checks the first item in the world list
    #to find where this one is positioned and sets pos from that.
    frame_pos_x = world[0][0][0]
    frame_pos_y = world[0][0][1]
    
    score_text = font.render("Your score: {}".format(snake.score),
                             False, (0,0,0))
    
    screen.fill((255, 255, 255))
    screen.blit(score_text, (40,300))
    
    for lines in world:
        for tiles in lines:
            for body in snake.body:

                if tuple(body) == tiles:
                    #Checks where the head of the snake is on the board.
                    pygame.draw.rect(screen, 0,(body[0], body[1],
                                                tile_width, tile_height))
                    
            if fruit_list[0].pos == tiles:
                pygame.draw.rect(screen, 155,
                                 (tiles[0], tiles[1], tile_width, tile_height))
            #Draws every rectangle in the playingfield
            #pygame.draw.rect(screen, 0,(tiles[0], tiles[1],
            #                          tile_width, tile_height), 1)

    pygame.draw.rect(screen, 0, (frame_pos_x, frame_pos_y, x_max, y_max), 1)
    
    pygame.display.update()

def find_window_y_coord(world, tile_height = 10):
    return tile_height * (len(world))

def find_window_x_coord(world, tile_width = 10):
    return tile_width * (len(world))
    
#Start phase choose field size
#choose speed of snake (pygmae.time.wait())

def main(screen, world, font):
    game_over = False
    snake = Snake(world)
    clock = pygame.time.Clock()
    fruit_list = []
    key_l = []
    
    while not game_over:

        if len(fruit_list) == 0:
            place_fruit(world, snake, fruit_list)
            
        render(screen, world, snake, fruit_list, font)

        pygame.display.flip()
        
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
        snake.update(key_l.pop(0), world, fruit_list)

    print("Your score ended as {}!".format(snake.score))
    
        #Gör en updatefunktion

def place_fruit(world, snake, fruit_list):
    """
    Places a fruit on the map by random x and y coord.
    """
    window_min_x = world[0][0][1]
    window_min_y = world[0][0][0]
    window_max_x = find_window_x_coord(world)
    window_max_y = find_window_y_coord(world)

    x_coord = random.randrange(window_min_x, window_max_x, 10)
    y_coord = random.randrange(window_min_y, window_max_y, 10)

    fruit_pos = (y_coord, x_coord)

    if list(fruit_pos) in snake.body:
        place_fruit(world, snake, fruit_list)
    else:
        fruit = Fruit(fruit_pos)
        fruit_list.append(fruit)

class Fruit:
    def __init__(self, position):
        self.pos = position
        self.score = 10
    
class Snake:
    def __init__(self, world):
        #This checks the world list row 0 item 5's Y-coordinate.
        self.x_coord = world[5][0][0]
        #This checks the world list row 3 item 0 X-coordinate.
        self.y_coord = world[0][3][1]
        #The current direction the snake is moving.
        self.direction = 274
        #If the snake eats an fruit, one shall be added.
        self.body = [[self.x_coord, self.y_coord]]
        
        self.score = 0

    def update(self, key, world, fruit_list):
        self.move(key)
        self.eat_fruit(fruit_list)
        
    def eat_fruit(self, fruit_list):
        """
        Handles adding bodyparts and adding score
        to the snake.
        """
        head = tuple(self.body[0])
        if fruit_list[0].pos == head:
            self.score += fruit_list[0].score

            last = self.body[len(self.body) - 1]
            
            if self.direction == 273:
                self.body.append([last[0], last[1] - 10])
                
            elif self.direction == 274:
                self.body.append([last[0], last[1] + 10])
                
            elif self.direction == 275:
                self.body.append([last[0] + 10, last[1]])

            elif self.direction == 276:
                self.body.append([last[0] - 10, last[1]])

            fruit_list.pop()
            
            #När kroppen är längre än huvud hamnar
            #den tredje delen ovanpå den andra, detta blir trubbel
            
        
    def move(self, key):
        """
        Moves the snake.
        """
        self.body_update()
        
        if key == "Not pressed":
            key = self.direction

        #up = 273
        #down = 274
        #right = 275
        #left = 276

        if key == 273:
            self.body[0][1] -= 10
                
        elif key == 274:
            self.body[0][1] += 10
            
        elif key == 275:
            self.body[0][0] += 10
                
        elif key == 276:
            self.body[0][0] -= 10

        self.direction = key        


    def body_update(self):
        """
        Checks the previous body part and updates position after that.
        """
        length = len(self.body) - 1
        while length >= 1:
            #This starts from the back of the worm and updates each
            #bodypart to be in the position of the index before. 
            self.body[length][0] = self.body[length - 1][0]
            self.body[length][1] = self.body[length - 1][1]
            length -= 1        
    
        
if __name__=='__main__':
    pygame.init()
    SCREEN_WIDTH = 424
    SCREEN_HEIGHT = 320
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((255, 255, 255))

    font = pygame.font.SysFont('Comic Sans MS', 30)
    
    world = create_map(SCREEN_WIDTH, SCREEN_HEIGHT)
    

    
    main(screen, world, font)
