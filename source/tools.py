import pygame
import random
import os

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((800,600))
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

    def run(self, state):
        GRAPHICS = load_graphics('resources/graphics')
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
                state.update(self.screen)
                pygame.display.update()
                # 数字越大 电脑负荷越大 画面越流畅
                self.clock.tick(60)

def load_graphics(path, accept=('.jpg','.png','.bmp','.gif')):
    graphics = {}
    for pic in os.listdir(path):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(path, pic))
            # 底层
            if img.get_alpha():
                img = img .convert_alpha()
            else:
                img = img.convert()
            graphics[name] = img
    return graphics
def get_image(sheet, x, y, width, height, colorkey, scale):
    image = pygame.Surface((width, height))
    image.blit(sheet, (0,0), (x,y,width,height))
    image.set_colorkey(colorkey)
    image = pygame.transform.scale(image, (int(width*scale),int(height*scale)))
    return image
    
