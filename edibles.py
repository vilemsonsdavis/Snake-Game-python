import pygame


class Fruit(object):
    w = 500
    rows = 20

    def __init__(self, start, edible):
        self.pos = start
        self.edible = edible

    def draw(self, surface):
        dis = self.w // self.rows
        i = self.pos[0]  # row
        j = self.pos[1]  # column

        surface.blit(self.edible, (self.pos[0]*dis, self.pos[1]*dis))