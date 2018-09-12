#class to store all the settings

class Settings():

    def __init__(self):
        #initialize game Settings
        #screen Settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (26, 48, 85)

        #ship Settings
        self.ship_speed_factor = 1.5

        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (46,148,60)
        self.bullets_allowed = 3
