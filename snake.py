from typing import Dict, Any

import cube
import pygame


class Snake(object):
    body = []
    turns = {}
    snakePics = [
        pygame.image.load('snake_pics/head_up.png'),
        pygame.image.load('snake_pics/head_down.png'),
        pygame.image.load('snake_pics/head_right.png'),
        pygame.image.load('snake_pics/head_left.png'),
        pygame.image.load('snake_pics/tail_up.png'),
        pygame.image.load('snake_pics/tail_down.png'),
        pygame.image.load('snake_pics/tail_left.png'),
        pygame.image.load('snake_pics/tail_right.png'),
    ]

    def __init__(self, color, pos):
        self.color = color
        self.head = cube.Cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
        self.prev_dir = 'down'
        self.head_pic = self.snakePics[1]
        self.tail_pic = self.snakePics[5]
        self.addCube()

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT] and (self.prev_dir != 'right' or len(self.body) < 3):
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    self.prev_dir = 'left'
                    self.head_pic = self.snakePics[3]
                elif keys[pygame.K_RIGHT] and (self.prev_dir != 'left' or len(self.body) < 3):
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    self.prev_dir = 'right'
                    self.head_pic = self.snakePics[2]
                elif keys[pygame.K_UP] and (self.prev_dir != 'down' or len(self.body) < 3):
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    self.prev_dir = 'up'
                    self.head_pic = self.snakePics[0]
                elif keys[pygame.K_DOWN] and (self.prev_dir != 'up' or len(self.body) < 3):
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    self.prev_dir = 'down'
                    self.head_pic = self.snakePics[1]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1], self.turns)
                if i == len(self.body)-2:
                    if turn[0] == 1:
                        self.tail_pic = self.snakePics[7]
                    if turn[0] == -1:
                        self.tail_pic = self.snakePics[6]
                    if turn[1] == -1:
                        self.tail_pic = self.snakePics[4]
                    if turn[1] == 1:
                        self.tail_pic = self.snakePics[5]
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                c.move(c.dirnx, c.dirny, self.turns)

    def reset(self, pos):
        self.head = cube.Cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1
        self.prev_dir = 'down'
        self.head_pic = self.snakePics[1]
        self.tail_pic = self.snakePics[5]
        self.addCube()

    def addCube(self):
        tail = self.body[-1] # last element
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(cube.Cube((tail.pos[0]-1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube.Cube((tail.pos[0]+1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube.Cube((tail.pos[0], tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube.Cube((tail.pos[0], tail.pos[1]+1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, self.head_pic, True)
            elif i+1 == len(self.body) and len(self.body) >= 2:
                c.draw(surface, self.tail_pic, True)
            else:
                c.draw(surface, None)