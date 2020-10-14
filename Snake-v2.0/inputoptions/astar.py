
class AStar():
    def __init__(self, world):
        self.current_path = []
        breadth = len(world[0])
        height = len(world)
        self.world_view = [[0] * (breadth - 1) for i in range(height)]

    def get_action(self, world, snake, fruit, pygame):
        """
        #up 119 W
        #down 115 S
        #right 97 D
        #left 100 A
        """
        
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                return "Quit"

        self.place_obsticals(snake, fruit, world)

        
    def place_obsticals(self, snake, fruit, world):

        # (xaxis, yaxis)
        fruit_pos = None

        """
        Kanske kan vara så att det går att endast göra denna om en nuvarande path ej finns, kan spara
        komplexitet

        if len(current_path) == 0:
        """
        # Place the snake and fruit on own world_view
        for row in range(len(world)):
            for cell in range(len(world[row])):
                for body_part in snake.body:

                    if tuple(body_part) == world[row][cell]:
                        # Set a obsticle within the A* world_view
                        self.world_view[row][cell] = -1
                    
                    elif fruit.pos == world[row][cell]:
                        fruit_pos = (cell, row)

                        self.world_view[row][cell] = 9999
        
        # 
        for row in range(len(self.world_view)):
            for value in range(len(self.world_view[row])):

                # Fruits and obsticles
                if self.world_view[row][value] == 9999 or self.world_view[row][value] == -1:
                    continue

                # From the perspective of the fruit, make a heuristic cost map
                # to then be able to create a path from the perspective of the snake
                # to the fruit.

                difference_y = abs(fruit_pos[1] - row)
                difference_x = abs(fruit_pos[0] - value)
                cell_value = difference_x + difference_y
                self.world_view[row][value] = cell_value


        for r in self.world_view:
            print(r)

