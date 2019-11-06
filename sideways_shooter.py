import pygame

class SW_Ship():

    def __init__(self, ai_settings, screen):

        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/sw_ship.bmp')

        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()

        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery
        
        self.bottom = float(self.rect.bottom)
        
        #self.moving_right = False
        #self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self):

        #if self.moving_right and self.rect.right < self.screen_rect.right :
            #self.centerx += self.ai_settings.sw_ship_speed_factor
        #if self.moving_left and self.rect.left > 0:
            #self.centerx -= self.ai_settings.sw_ship_speed_factor

        #if self.moving_up and self.rect.top > self.screen_rect.top:
        if self.moving_up and self.rect.top > self.screen_rect.top:
            #self.centery -= self.ai_settings.sw_ship_speed_factor
            self.bottom -= self.ai_settings.sw_ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            #self.centery += self.ai_settings.sw_ship_speed_factor
            self.bottom += self.ai_settings.sw_ship_speed_factor
            
        #if self.moving_up or self.moving_down:
        self.rect.bottom = self.bottom
            
        #if self.moving_left or self.moving_right:
            #self.rect.centerx = self.centerx
        
    def blitme(self):

        self.screen.blit(self.image, self.rect)
