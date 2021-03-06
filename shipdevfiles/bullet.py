import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #manages bullet fired at ships

    def __init__(self, ai_set, screen, ship):
        # create bullet at ship position
        super(Bullet, self).__init__()
        self.screen = screen

        #create bullet at (0,0) and set correct position
        self.rect = pygame.Rect(0,0, ai_set.bullet_width, ai_set.bullet_height)
        self.rect.centerx = ship.rect.right #positioning bullet to ship
        self.rect.top = ship.rect.centery #stay on top of ship as it's firing

        #store bullet position as decimal value so you can move it
        self.x = float(self.rect.x)

        self.color = ai_set.bullet_color
        self.speed_factor = ai_set.bullet_speed_factor

    def update(self):
        #move bullet up the screen by updating y decimal
        self.x += self.speed_factor
        #update the rectangle position
        self.rect.x = self.x

    def draw_bullet(self):
        #draw bullet to screen
        pygame.draw.rect(self.screen, self.color, self.rect)
