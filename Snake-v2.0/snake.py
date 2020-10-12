class Snake:
    def __init__(self, world, config):
        self.x_coord = world[0][2][0]
        self.y_coord = world[2][0][1]
        #The current direction the snake is moving.
        self.direction = 0
        #If the snake eats an fruit, one shall be added.
        self.body = [[self.x_coord, self.y_coord]]
        self.alive = True
        self.score = 0
        self.immortal = config.settings["Immortal"]
        #self.speed = config.settings["Snake speed"]

    def update(self, key, world, fruit_list):
        self.move(key)

        if not self.immortal:
            self.check_dead(world)
        
        self.eat_fruit(fruit_list)

    def check_dead(self, world):
        head = tuple(self.body[0])
        self.alive = False
                
        for row in world:
            if head in row:
                self.alive = True

        #If the head coordinates are in the body, the head eats the body.
        if self.body[0] in self.body[1:]:
            self.alive = False
        
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

        # TODO Tänk över om direciton kommer att stämma genom att
        # endast titta på vilken sista key som blev klickad är korrekt (tänk ned och sväng ex)
        self.direction = key        

    def body_update(self):
        """
        Checks the previous body part and updates position after that.
        """
        length = len(self.body) - 1
        while length >= 1:
            # This starts from the back of the worm and updates each
            # bodypart to be in the position of the index before. 
            self.body[length][0] = self.body[length - 1][0]
            self.body[length][1] = self.body[length - 1][1]
            length -= 1
