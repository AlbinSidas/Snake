class Human():

    def get_action(self, world_list, python, fruit, pygame):

        key_l = []
        for event in pygame.event.get():
            pressed_key = "Not pressed"
        
            if event.type == pygame.locals.QUIT:
                pressed_key = "Quit"
            elif event.type == pygame.locals.KEYDOWN:
                pressed_key = event.key
            
            key_l.append(pressed_key)

        if len(key_l) == 0:
            key_l.append("Not pressed")

        action = key_l.pop(0)
                
        return action