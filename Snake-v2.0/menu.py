import pygame
import pygame.locals
import game_state
import config

class Menu:

    def __init__(self):
        self.config_object = config.Config("config.txt")

        # Looks inside the config file and retrieves the windowsize from there.
        self.screen_height, self.screen_width = \
                                self.config_object.settings["Screensize"].split("x")
        self.screen_height = int(self.screen_height)
        self.screen_width = int(self.screen_width)                                      
        
    def start(self):
        pygame.init()
        screen = pygame.display.set_mode((self.screen_height, self.screen_width))
        font = pygame.font.SysFont('Comic Sans MS', 30)
        clock = pygame.time.Clock()
        
        # Checks if user wants to close the game. 
        shut_down = False
        # This will mark the current choosen menu alternative.
        choice = 0
        # This will hold information about which keys has been pressed this loop.
        key_list = []
        # Outcome-list will hold information about the game,
        # if exited or if it should add new scores to highscore etc.
        outcome = []

        # Converts a keystroke value (up, down, right, left) to values to
        # add to choice.
        key_converter = {
            "273" : -1,
            "274" : 1,
            "275" : 1,
            "276" : -1
        }
        
        while not shut_down:

            self.render(screen, font, choice)#, self.screen_height, self.screen_width)
            
            pressed_key = "Not pressed"
            
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    shut_down = True
                elif event.type == pygame.locals.KEYDOWN:
                    # Converted because this is the key in the converter.
                    pressed_key = str(event.key)

            if pressed_key != "Not pressed": 
                key_list.append(pressed_key)
            
            if len(key_list) != 0:
                key = key_list.pop()
                if key in key_converter:
                    
                    choice += key_converter[key]
                    if choice > 2:
                        choice = 0
                    elif choice < 0:
                        choice = 2
                        
                elif key == "13":
                    # TODO
                    if choice == 0:
                        print(self.config_object)
                        start_game = game_state.Game_State(self.config_object)

                        outcome = start_game.start(screen, font)
                        
                    elif choice == 1:
                        outcome = self.config_object.start(screen, key_converter, font,
                                                           self.screen_height, self.screen_width)
                    elif choice == 2:
                        shut_down = True

                    if len(outcome) > 0:
                        length = len(outcome)
                        if outcome[length - 1] == 0:
                            # Outcome is only returned if the player wants to exit. 
                            shut_down = True
                            
                        elif outcome[length - 3] == 10:
                            # Here I check the returnvalues if the screensize
                            # was changed in the config object.
                            self.screen_height = int(outcome[length - 2])
                            self.screen_width = int(outcome[length - 1])                    
                    
            clock.tick(10)
                    
    def render(self, screen, font, choice):#, sw, sh):
        menu_title = self.text(font, "Menu")
        start = self.text(font, "Start")
        settings = self.text(font, "Settings")
        quiit = self.text(font, "Quit")
        sh = self.screen_height
        sw = self.screen_width
        
        if choice == 0:
            start = self.text(font, "Start", (220,20,60))
        elif choice == 1:
            settings = self.text(font, "Settings", (220, 20, 60))
        elif choice == 2:
            quiit = self.text(font, "Quit", (220 , 20, 60))
             
        screen.fill((255,255,255))
        screen.blit(menu_title, (sw/2, sh / 10))
        screen.blit(start, (sw/2, sh / 3))
        screen.blit(settings, (sw/2 - sw/40, sh / 2))
        screen.blit(quiit, (sw/2 , sh / 1.5))
        
        pygame.display.update()
        pygame.display.flip()
        
    def text(self, font, text, color = (11,102,35)):
        return font.render(text, False, color)

if __name__ == '__main__':
    m = Menu()
