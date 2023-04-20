import pygame as pg
import math 

from settings import *

class RayCast:
    
    def __init__(self, game):
        
        self.game = game
    
    def rays(self):
        
        x_map, y_map = self.game.player.map_pos
        ox, oy = self.game.player.map
        
        ray_angle = self.game.player.angle - (FOV / 2) + 0.0001
        
        for ray in range(NUM_RAYS):
            
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)
            
            # horizontals
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (x_map - 1e-6, -1)
            depth_hor = (y_map - oy) / sin_a
            x_hor = ox + depth_hor * cos_a
            
            delta_depth = dy / sin_a
            dx = delta_depth * cos_a
            
            for i in range(MAX_DEPTH):
                
                tile_hor = int(x_hor), int(y_hor)
                
                if tile_hor in self.game.world_map:

                    break
                
                x_hor += dx
                y_hot += dy
                depth_hor += delta_depth
            
            
            # verticals
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)
            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a
            
            delta_depth = dx / cos_a
            dy = delta_depth * sin_a
            
            for i in range(MAX_DEPTH):
                
                tile_vert = int(x_vert), int(y_vert)
                
                if tile_vert in self.game.map.world_map:
                    
                    break
                
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth
            
            ray_angle += DELTA_ANG
    
    def update(self):
        self.rays()