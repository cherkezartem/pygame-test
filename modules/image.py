import pygame
import os


class Img():
    def __init__(self, width, height, name, x, y):
        self.width = width
        self.height = height
        self.name = name
        self.x = x 
        self.y = y 
        self.load_image()
    def load_image(self):
        path = os.path.abspath(os.path.join(__file__, "..", "..", "img", self.name))
        image = pygame.image.load(path)
        self.image = pygame.transform.scale(image, (self.width, self.height))
    def show_image(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))


img1 = Img(100, 150, "img.png", 0, 0)
img2 = Img(300, 400, "img.png", 500, 100)

