
class AStar():
    """
    Should implement within the catch statement that
    a new path is being calculated with other order of 
    actions to see if it can find a path that conforms
    """
    def __init__(self, world):
        self.current_path = []
        self.history = []
        breadth = len(world[0])
        height = len(world)
        self.world_view = [[0] * (breadth - 1) for i in range(height)]

    def get_action(self, world, snake, fruit, pygame):
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                return "Quit"
        
        snake_head = self.get_snake_head(world, snake)

        if len(self.current_path) != 0:
            return self.astar_action(snake_head)
            
        # Inject the snakebody and fruits into own worldview
        fruit_pos = self.place_obsticals(snake, fruit, world) 
        
        # Build the heuristic cost map
        self.build_starmap(fruit_pos)
        
        # Builds the current path
        try: 
            self.build_path(snake_head)
        except:
            print("Har en ickefullpath")
            """
            Kan jag här försöka hantera att den ska göra en path där 
            den bara håller sig vid liv på ytan den har just då?

            Genom att ta den första i pathen blir det problematiskt eftersom den kommer gå närmare att inte ha någonstans att gå

            randomisera ordningen på actionsen ? kan jag på något sätt försöka ta en annan path

            möjligen söka efter path i en annan ordning göra build path med annan ordning
            """

            self.current_path.reverse()
            action = self.astar_action(snake_head)
            self.current_path = []
            return action

        #Turn the path around to not move the whole array for each pop
        self.current_path.reverse()
        #print(self.current_path)
        return self.astar_action(snake_head)

    def astar_action(self, head):
        go_to = self.current_path.pop()
        
        action = "No action"
                
        # INT VALUE FOR DIRECTIONS
        #up = 273
        #down = 274
        #right = 275
        #left = 276

        #up 119 W
        #down 115 S
        #right 97 D
        #left 100 A

        if go_to[0] < head[0]:
            # Target is above head
            return 119

        elif go_to[0] > head [0]:
            # Target is below head
            return 115

        if go_to[1] < head[1]:
            # Target left of the head
            return 276

        elif go_to[1] > head [1]:
            # Target to the right of the head
            return 275

    def get_snake_head(self, world, snake):
        head = tuple(snake.body[0])

        for row in range(len(world)):
            for ycell in range(len(world[row])):
                if world[row][ycell] == head:                    
                    return (row, ycell)

    def build_path(self, snake_head):
        direction_values = self.get_direction_values(snake_head)
 
        minimum = 9999
        #minimum = 99999
        
        go_to = None
        
        for direction in direction_values:
            if direction[0] < minimum and direction[1] not in self.current_path:
                minimum = direction[0]
                go_to = direction[1]
        
        if minimum == -1:
            self.current_path.append(go_to)
            return 
        else:
            self.current_path.append(go_to)
            
            return self.build_path(go_to)

    
    def get_direction_values(self, snake_head):
        # Outer bounds of the world
        max_height = len(self.world_view)
        max_width = len(self.world_view[0])

        # Add the values and coordinates for the next move
        direction_values = []
        if snake_head[0] - 1 >= 0 and snake_head[0] < max_height:
            move_head_to = (snake_head[0] - 1, snake_head[1])
            direction_values.append([self.world_view[snake_head[0] - 1][snake_head[1]], move_head_to])
        else:
            # If the values are not within the map
            direction_values.append([9999, snake_head])

        if snake_head[0] + 1 < max_height:
            move_head_to = (snake_head[0] + 1, snake_head[1])
            direction_values.append([self.world_view[snake_head[0] + 1][snake_head[1]], move_head_to])
        else:
            direction_values.append([9999, snake_head])

        if snake_head[1] - 1 >= 0 and snake_head[1] < max_width:
            move_head_to = (snake_head[0], snake_head[1] - 1)
            direction_values.append([self.world_view[snake_head[0]][snake_head[1] - 1], move_head_to])
        else:
            direction_values.append([9999, snake_head])

        if snake_head[1] + 1 < max_width:
            move_head_to = (snake_head[0], snake_head[1] + 1)
            direction_values.append([self.world_view[snake_head[0]][snake_head[1] + 1], move_head_to])
        else:
            direction_values.append([9999, snake_head])

        return direction_values

    def place_obsticals(self, snake, fruit, world):

        # (xaxis, yaxis)
        fruit_pos = None
        
        # Reset world_view map
        self.world_view = [[0] * (len(world[0]) - 1) for i in range(len(world))]

        # Place the snake and fruit on own world_view
        for row in range(len(world)):
            for cell in range(len(world[row])):
        
                for body_part in snake.body:
                    if tuple(body_part) == world[row][cell]:
                        # Set a obsticle within the A* world_view
                        self.world_view[row][cell] = 9999
                    
                if fruit.pos == world[row][cell]:
                    fruit_pos = (cell, row)

                    self.world_view[row][cell] = -1

                
        return fruit_pos

    def build_starmap(self, fruit_pos):
        # Build starmap
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


