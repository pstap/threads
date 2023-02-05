import pygame
from pygame import gfxdraw
import numpy as np
from numpy import pi
from random import randint


def rot_matrix_2d(angle):
    r1 = [np.cos(angle), -1 * np.sin(angle)]
    r2 = [np.sin(angle), np.cos(angle)]
    return np.matrix([r1,r2])

def rotate_point(point, origin, angle):
    rot_mat = rot_matrix_2d(angle)
    point = np.matrix([origin[1] - point[1], origin[0] - point[0]])
    temp = rot_mat * point.T
    temp = temp + np.matrix([origin[1], origin[0]])
    return temp.T

class Window:
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWSURFACE)
        self.width = width
        self.height = height

    def save(self, path):
        pygame.image.save(self.screen, path)

    def set_pixel(self, position, color):
        #x = round(position.item(0,0))
        #y = round(position.item(0,1))
        x = int(position[0])
        y = int(position[1])
        gfxdraw.pixel(self.screen, x, y, color)
        #self.screen.fill(color, ((x,y), (1,1)), 2)

    def clear(self):
        #self.screen.fill((0,0,0))
        self.screen.fill((255,255,255))

    def line(self,p1, p2, color):
        pygame.draw.line(self.screen, color, p1, p2, 1)

    def circle(self, p, r, color):
        x = int(p[0])
        y = int(p[1])
        pygame.draw.circle(self.screen, color, (x,y), round(r), 0)

    def mid(self):
        return (self.width / 2, self.height / 2)

def rand2(max1, max2):
    return (randint(0, max1), randint(0, max2))

def midpoint(p1, p2):
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]

    return (abs((x2 - x1)/2), abs((y2 - y1) / 2))

def main():
    pygame.init()
    window = Window(600, 600)
    done = False


    points = []
    cycles = 1
    step = (2*pi) / (window.width / cycles)
    for x in range(0, window.width):
        points.append(np.sin(x * step))

    i = 0
    z = 2
    direction = 1
    prev = (0,0)
    saved = False
    colors = [(200,255,255), (255, 255, 200), (255, 200, 255)]
    while not done:
        window.clear()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True


        first = True
        #for p in range(0, window.width, round(z/4) + 1):
        for p in range(30, window.width - 30, 11):
            y = (window.height / 2) + 80 * points[(i+p) % window.width]
            #yn = (window.height / 2) + -50 * points[(i+p+10) % window.width]
            dx = abs((window.width / 2) - p)
            yo = y
            y = y - (150 * (dx / window.height))
            #origin = midpoint((p,y), (window.width / 2, window.height / 2))
            #origin = (window.width/2, 100 + 50 * points[(i+p) % window.width])
            origin = midpoint((0,0), (window.width, 0))
            #f = (abs((window.width / 2) - p ) / (window.width / 2))
            f = 1
            # Really interesting line
            #window.line((p,y), (window.width / 2 - (p / 2), window.height/2), (f*150,f*150,f*150))
            #window.line((p,y), (window.width / 2 + (p / 2), yo), (f*150,f*150,f*150))
            #window.line(midpoint((p,y), window.mid()), (p,y), (f*150,f*150,f*150))
            #window.line((p,y), (window.width/2, window.height/2 + 150), (200,200,200))

            #if p < (window.width / 2):
                #window.line((p,y), origin, ((f*220, f*220,f*220)))
                #window.line((p,y), (p, window.height), (240,240,240))
            #else:
                #window.line((p,y), (p, window.height), (240,240,240))            
                #window.line((p,y), origin, ((f*220, f*220,f*220)))

            window.line((y,p), (p,yo), ((150, 150, 150)))

            # Cennect end points
            #if first:
                #first = False
            #else:
                #window.line((p,y), prev, (100,100,100))
            #window.circle((window.width / 2 + (p / 2), yo), 3, (100,100,100))
            #window.circle((p,y), 3, (100,100,100))
            #window.circle(midpoint((p,y), window.mid()), 3, (100, 100, 100))
            window.circle((y,p), 3, (100,100,100))
            window.circle((p,yo), 3, (100,100,100))
            prev = (p,y)

        #window.line((0,500), (window.width, 500), (100,60,0))
        pygame.display.flip()
       
        print(f"saving {i}.png")
        pygame.image.save(window.screen, f"./out/{i}.png")

        i = (i + 1) % window.width
        if i > window.width:
            done = True

        #if z == 60:
        #    direction = -1
        #if z == 4:
        #    direction = 1

        #z += direction
        
        # pygame.time.wait(10)
                

if __name__ == "__main__":
    main()
