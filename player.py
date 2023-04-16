import pygame as pg
import math

from settings import *

class Player:
    
    def __init__(self, game):
        
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANG
    
    def movement(self):
        
        # movement speed and rotation speed initialization
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        
        dx, dy = 0, 0
        
        speed = PLAYER_SPD * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a
        
        keys = pg.key.get_pressed()
        
        # movement keys settings
        if keys[pg.K_w]:
            
            #dx, dy = dx + speed_sin, dy + speed_cos
            dx += speed_cos
            dy += speed_sin 
            
        if keys[pg.K_s]:
            
            #dx, dy = dx - speed_sin, dy - speed_cos
            dx += -speed_cos
            dy += -speed_sin 
            
        if keys[pg.K_d]:
            
            #dx, dy = dx - speed_sin, dy + speed_cos
            dx += -speed_cos
            dy += speed_sin 
        
        if keys[pg.K_a]:
            
            #dx, dy = dx + speed_sin, dy - speed_cos
            dx += speed_cos
            dy += -speed_sin 

        #self.x += dx
        #self.y += dy
        
        self.collision(dx, dy)
        
        # rotation keys settings
        if keys[pg.K_LEFT]:
            
            self.angle -= PLAYER_ROT * self.game.delta_time
                        
        if keys[pg.K_RIGHT]:
            
            self.angle += PLAYER_ROT * self.game.delta_time
        
        self.angle %= math.tau # 2*pi
    
    # wall and collision settings
    def wall(self,x, y):
        
        return (x, y) not in self.game.map.worldmap
    
    def collision(self, dx, dy):

        if self.wall(int(self.x + dx), int(self.y)):
            
            self.x += dx
        if self.wall(int(self.x), int(self.y + dy)):
             
            self.y += dy
    
    # player and player's vision visualization
    def draw(self):
        
        pg.draw.line(self.game.screen, 'blue', (self.x * 100, self.y * 100,), (self.x * 100 + WIDTH * math.cos(self.angle), self.y * 100 + WIDTH * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15) 
    
    def update(self):
        
        self.movement()
        
    @property
    def pos(self):
        
        return self.x, self.y
    
    @property
    def map_pos(self):
        
        return int(self.x), int(self.y)

        