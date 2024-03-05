import pygame
import math
from ..color import Color


def get_coord_line(x1, y1, Rx, Ry, L):
    dx = Rx - x1
    dy = Ry - y1
    
    distance = math.sqrt(dx**2 + dy**2)
    
    ux = dx / distance
    uy = dy / distance
    
    vx = ux * L
    vy = uy * L
    
    x2 = x1 + vx
    y2 = y1 + vy
    return x2, y2

class Cuboid:
    def __init__(self, x, y, l, screen = None):
        self.x = x
        self.y = y
        self.l = l
        self.screen = screen
        
    def draw(self, vanish_points):
        if len(vanish_points) == 1:
            self._draw_1_vanish_point(vanish_points)
    
    def _draw_1_vanish_point(self, vanish_points):
        VPx, VPy = vanish_points[0][0], vanish_points[0][1]
        coords = {
            "p1": (self.x, self.y),
            "p2": (self.x + self.l, self.y),
            "p3": (self.x + self.l, self.y + self.l),
            "p4": (self.x, self.y + self.l),
            "p5": get_coord_line(self.x, self.y, VPx, VPy, 50),
            "p6": get_coord_line(self.x + self.l, self.y, VPx, VPy, 50),
            "p7": get_coord_line(self.x + self.l, self.y + self.l, VPx, VPy, 50),
            "p8": get_coord_line(self.x, self.y + self.l, VPx, VPy, 50),
        }
        f1 = [coords["p5"], coords["p6"], coords["p7"], coords["p8"]] 
        
        f2 = [coords["p8"], coords["p7"], coords["p3"], coords["p4"]]
        f3 = [coords["p1"], coords["p5"], coords["p8"], coords["p4"]]
        f4 = [coords["p1"], coords["p5"], coords["p6"], coords["p2"]]
        f5 = [coords["p2"], coords["p6"], coords["p7"], coords["p3"]]
        
        f6 = [coords["p1"], coords["p2"], coords["p3"], coords["p4"]]
        
        #z1 = 
        

        for points, color in [(f1, Color.WHITE), (f2, Color.WHITE), (f3, Color.ORANGE), (f4, Color.GREEN), (f5, Color.BLUE), (f6, Color.RED)]:
            pygame.draw.polygon(self.screen, color.rgb, points)
        
        
    
    