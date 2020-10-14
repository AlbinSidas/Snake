
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
        
        if len(self.current_path) != 0:
            
            return
            
        fruit_pos = self.place_obsticals(snake, fruit, world)        
        self.build_starmap(fruit_pos)
        
        self.get_best_direction(world, snake)

        for r in self.world_view:
            print(r)


        """
        Titta på var huvud är, kolla sedan på current_path om den inte är tom
        då ska ormen ta den SISTA i listan (
            current_path.pop()  )
        
        Utifrån den koordinaten, skicka tillbaka en action som säger var ormen ska gå.

        """
    
    def get_best_direction(self, world, snake):
        """
        TODO
        DENNA HITTAR BARA HUVUDET JUST NU GANSKA VÄRDELÖS
        """
        
        # INT VALUE FOR DIRECTIONS
        #up = 273
        #down = 274
        #right = 275
        #left = 276

        #up 119 W
        #down 115 S
        #right 97 D
        #left 100 A

        #direction = snake.direction

        head = tuple(snake.body[0])

        def find_head_in_world(world, snake):
            for row in range(len(world)):
                for ycell in range(len(world[row])):
                    if world[row][ycell] == head:
                        
                        #snake_head_indexes = 
                        return (row, ycell)
                        #break 

        snake_head_indexes = find_head_in_world(world, snake)
        
        self.build_path(snake_head_indexes)

        """
        Sätt det nedan till en while loop tills målet 
        är hittat för att bygga upp pathen till målet
        
        När jag fått ut direction values och tillhörande koordinater (alltså i vilka index
        som ormhuvudet nu står i (vilket är nästa steg efter en iteration)) så kör det igen

        En rekursiv funktion ^
        """


    def build_path(self, snake_head):
        direction_values = self.get_direction_values(snake_head)
        
        minimum = 9999
        go_to = None
        for direction in direction_values:
            if direction[0] < minimum: 
                minimum = direction[0]
                go_to = direction[1]


        if minimum == -1:
            self.current_path.append(go_to)
            return 
        else:
            #print(minimum)
            self.current_path.append(go_to)
            return self.build_path(go_to)

        #print(self.current_path)
        #print(minimum)
        #print(go_to)
        """
        Titta runt ormen i self.world_view
        hita maxvärdet runt ormen
        skicka tillbaka rätt intväde baserat på detta
        """
    
    def get_direction_values(self, snake_head):
        
        """
        kontrollera att x - 1, x + 1, y - 1, y + 1 finns i world_view
        """
        
        max_height = len(self.world_view)
        max_width = len(self.world_view[0])
        
        """
        Kanske måste returnera vilken index i världen den är i den nya
        så jag kan bygga en path
        """

        # snake_head = (y, x)
        direction_values = []
        if snake_head[0] - 1 >= 0 and snake_head[0] < max_height:
            
            move_head_to = (snake_head[0] - 1, snake_head[1])
            direction_values.append([self.world_view[snake_head[0] - 1][snake_head[1]], move_head_to])
        else:
            direction_values.append(9999)

        if snake_head[0] + 1 < max_height:
            move_head_to = (snake_head[0] + 1, snake_head[1])
            direction_values.append([self.world_view[snake_head[0] + 1][snake_head[1]], move_head_to])

            #direction_values.append(self.world_view[snake_head[0] + 1][snake_head[1]], ([snake_head[0] + 1, snake_head[1]))
        else:
            direction_values.append(9999)

        if snake_head[1] - 1 >= 0 and snake_head[1] < max_width:
            move_head_to = (snake_head[0], snake_head[1] - 1)
            direction_values.append([self.world_view[snake_head[0]][snake_head[1] - 1], move_head_to])

            #direction_values.append(self.world_view[snake_head[0]][snake_head[1] - 1], (snake_head[0], snake_head[1] - 1))
        else:
            direction_values.append(9999)

        if snake_head[1] + 1 < max_width:
            move_head_to = (snake_head[0], snake_head[1] + 1)
            direction_values.append([self.world_view[snake_head[0]][snake_head[1] + 1], move_head_to])

            #direction_values.append(self.world_view[snake_head[0]][snake_head[1] + 1], (snake_head[0], snake_head[1] + 1))
        else:
            direction_values.append(9999)

        
        return direction_values


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
                        self.world_view[row][cell] = 9999
                    
                    elif fruit.pos == world[row][cell]:
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


