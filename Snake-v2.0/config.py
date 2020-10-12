import pygame
import pygame.locals
import re

class Config:

    def __init__(self, filename):
        self.settings = {}

        with open(filename, 'r') as f:
            self.settings = self.setting_categories(f)

        print(self.settings)
            
    def setting_categories(self, config_file):
        settings = {}
        
        for line in config_file:
            line = line.split(":")
            
            if len(line) > 1:
                if '\n' in line[1]:
                    # After the split this checks we if there's a newline
                    # if so, it's removed.
                    line[1] = line[1][:-1]

                if line[1] == "True" or line[1] == "False":
                    line[1] = True if line[1] == "True" else False
                    
                settings[line[0]] = line[1]

        return settings

    def start(self, screen, key_converter, font, screen_width, screen_height):
        
        clock = pygame.time.Clock()        
        choice = 0
        key_list = []
        exit_settings = False
        screen_change_made = False
        outcome = []
        
        while not exit_settings:
            
            if not screen_change_made:
                self.render(screen, font, choice, screen_width, screen_height)
            else:
                screen_width, screen_height = self.settings["Screensize"].split("x")
                screen_width = int(screen_width)
                screen_height = int(screen_height)
                self.render(screen, font, choice, screen_width, screen_height)
                screen_change_made = False
            
            pressed_key = "Not pressed"
            
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                     return [0]
                elif event.type == pygame.locals.KEYDOWN:
                    # Converted because this is the key in the converter.
                    pressed_key = str(event.key)

            if pressed_key != "Not pressed": 
                key_list.append(pressed_key)
            
            if len(key_list) != 0:
                key = key_list.pop()
                if key in key_converter:
                    
                    choice += key_converter[key]
                    if choice > 6:
                        choice = 0
                    elif choice < 0:
                        choice = 6
                        
                elif key == "13":
                    if choice == 0:
                        self.settings["Boardsize"] = self.change_integer_value(self.settings["Boardsize"], 10, 20, 2)
                        self.update_config_file("Boardsize", self.settings["Boardsize"])
                        
                    elif choice == 1:
                        alternatives = ["1024x800", "700x600", "424x300"]
                        ind = alternatives.index(self.settings["Screensize"])
                        ind += 1
                        
                        if ind + 1 > len(alternatives):
                            ind = 0
                            
                        self.settings["Screensize"] = alternatives[ind]
                        height, width = self.settings["Screensize"].split("x")
                        pygame.display.set_mode((int(height), int(width)))

                        self.update_config_file("Screensize", alternatives[ind])
                        
                        screen_change_made = True
                        outcome.append(10)
                        outcome.append(height)
                        outcome.append(width)
                        
                    elif choice == 2:
                        self.settings["Snake speed"] = self.change_integer_value(self.settings["Snake speed"], 5, 12, 1)
                        self.update_config_file("Snake speed", self.settings["Snake speed"])
                        
                    elif choice == 3:
                        self.settings["Immortal"] = self.change_boolean_value(bool(self.settings["Immortal"]))
                        self.update_config_file("Immortal", self.settings["Immortal"])
                        
                    elif choice == 4:
                        self.settings["Two player"] = self.change_boolean_value(bool(self.settings["Two player"]))
                        self.update_config_file("Two player", self.settings["Two player"])
                                                
                    elif choice == 5:
                        # Back to menu
                        return outcome
                    elif choice == 6:
                        # Quit the game
                        outcome.append(0)
                        return outcome
                    
            clock.tick(10)
    
                    
    def render(self, screen, font, choice, sw, sh):
        import pygame
        settings = self.text(font, "Settings")
        
        world = self.text(font, "World")
        board_size = self.text(font, "Boardsize: {}".format(self.settings["Boardsize"]))
        screen_size = self.text(font, "Screensize: {}".format(self.settings["Screensize"]))
        
        snake = self.text(font, "Snake")
        speed = self.text(font, "Speed: {}".format(self.settings["Snake speed"]))
        immortal = self.text(font, "Immortal: {}".format(self.settings["Immortal"]))
        
        two_player = self.text(font, "Two Player: {}".format(self.settings["Two player"]))
        
        menu = self.text(font, "Menu")
        
        quiit = self.text(font, "Quit")
        
        if choice == 0:
            board_size = self.text(font, "Boardsize: {}".format(self.settings["Boardsize"]), (220,20,60))
        elif choice == 1:
            screen_size = self.text(font, "Screensize: {}".format(self.settings["Screensize"]), (220, 20, 60))
        elif choice == 2:
            speed = self.text(font, "Speed: {}".format(self.settings["Snake speed"]), (220 , 20, 60))
        elif choice == 3:
            immortal = self.text(font, "Immortal: {}".format(self.settings["Immortal"]), (220 , 20, 60))
        elif choice == 4:
            two_player = self.text(font, "Two Player: {}".format(self.settings["Two player"]), (220 , 20, 60))
        elif choice == 5:
            menu = self.text(font, "Menu", (220 , 20, 60))
        elif choice == 6:
            quiit = self.text(font, "Quit", (220 , 20, 60))
            

        screen.fill((255,255,255))
        screen.blit(settings, (sw/2 - (sw/10), sh / 12))

        screen.blit(world, (sw/2 - (sw/2.5), sh / 6))
        screen.blit(board_size, (sw/2 - (sw/2.5), sh / 2.6))
        screen.blit(screen_size, (sw/2 - (sw/2.5), sh / 2))

        screen.blit(snake, (sw/2 + (sw/14), sh / 6))        
        screen.blit(speed, (sw/2 + (sw/14), sh / 2.6))
        screen.blit(immortal, (sw/2 + (sw/12), sh / 2))

        screen.blit(two_player, (sw/2 - (sw/10), sh / 2 + sh/10))
        
        screen.blit(menu, (sw/2 - (sw/3), sh / 1.2))        
        screen.blit(quiit, (sw/2 + sw/5, sh / 1.2))

        pygame.display.update()
        pygame.display.flip()
        
    def text(self, font, text, color = (11,102,35)):
        return font.render(text, False, color)

    def update_config_file(self, option, value):
        """
        Updates the config.txt with new a new value for selected option. 
        """
        data = []
        with open("config.txt", 'r') as f:    
            for line in f:
                data.append(line)

        data = self.update_line(data, option, value)

        updated_file = ""
        for row in data:
            updated_file += row

        with open("config.txt", 'w') as f:
            f.write(updated_file)
            
        
    def update_line(self, data, option, value):
        """
        Function that iterates the data and updates value,
        returns the data as a list as sent in. 
        """
        for ind, row in enumerate(data, 0):
            
            if option in row:
                values = row.split(":")
                values[1] = str(value) + "\n"
                connector = ":"
                data[ind] = connector.join(values)

        return data
    
    def change_integer_value(self, value, low, high, incr):
        try:
            value = int(value)
            value += incr
        except:
            value += incr

        
        if value > high:
            value = low
            return value

        return value

    def change_boolean_value(self, value):
        if value:
            return False

        return True
            
if __name__ == '__main__':
    #   import pygame.locals
    pygame.init()
    screen = pygame.display.set_mode((700, 600))
    font = pygame.font.SysFont('Comic Sans MS', 30)
    key_converter = {
        "273" : -1,
        "274" : 1,
        "275" : 1,
        "276" : -1
    }
    
    c = Config("config.txt")
    c.start(screen, key_converter, font, 700, 600)
