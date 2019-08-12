import pygame


class Cube(object):
    rows = 20
    w = 500
    cubePics = [
        pygame.image.load('snake_pics/turn1.png'),
        pygame.image.load('snake_pics/turn2.png'),
        pygame.image.load('snake_pics/turn3.png'),
        pygame.image.load('snake_pics/turn4.png'),
        pygame.image.load('snake_pics/horizontal.png'),
        pygame.image.load('snake_pics/vertical.png'),
    ]

    def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
        self.pos = start
        self.dirnx = 0
        self.dirny = 1
        self.color = color
        self.pic = None
        self.next_dir = None

    def move(self, dirnx, dirny, turns):

        self.dirnx = dirnx
        self.dirny = dirny

        if self.dirnx == -1:
            self.next_dir = 'left'
        if self.dirnx == 1:
            self.next_dir = 'right'
        if self.dirny == -1:
            self.next_dir = 'up'
        if self.dirny == 1:
            self.next_dir = 'down'

        nextPos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

        if self.pos[0] == 0 and self.next_dir == 'left':
            nextPos = (19, nextPos[1])
        if self.pos[0] == 19 and self.next_dir == 'right':
            nextPos = (0, nextPos[1])
        if self.pos[1] == 0 and self.next_dir == 'up':
            nextPos = (nextPos[0], 19)
        if self.pos[1] == 19 and self.next_dir == 'down':
            nextPos = (nextPos[0], 0)

        #TURNS
        if nextPos in turns:
            nextPosDir = turns[nextPos]

            if nextPosDir[0] == -1:
                self.next_dir = 'left'
            if nextPosDir[0] == 1:
                self.next_dir = 'right'
            if nextPosDir[1] == -1:
                self.next_dir = 'up'
            if nextPosDir[1] == 1:
                self.next_dir = 'down'

            if self.dirnx == -1:
                if self.next_dir == 'down':
                    self.pic = self.cubePics[0]
                if self.next_dir == 'up':
                    self.pic = self.cubePics[2]
            if self.dirnx == 1:
                if self.next_dir == 'down':
                    self.pic = self.cubePics[1]
                if self.next_dir == 'up':
                    self.pic = self.cubePics[3]
            if self.dirny == -1:
                if self.next_dir == 'left':
                    self.pic = self.cubePics[1]
                if self.next_dir == 'right':
                    self.pic = self.cubePics[0]
            if self.dirny == 1:
                if self.next_dir == 'left':
                    self.pic = self.cubePics[3]
                if self.next_dir == 'right':
                    self.pic = self.cubePics[2]
        #HORIZONTAL/VERTICAL
        if self.dirnx == 1 and self.next_dir == 'right':
            self.pic = self.cubePics[4]
        if self.dirnx == -1 and self.next_dir == 'left':
            self.pic = self.cubePics[4]
        if self.dirny == 1 and self.next_dir == 'down':
            self.pic = self.cubePics[5]
        if self.dirny == -1 and self.next_dir == 'up':
            self.pic = self.cubePics[5]

        #MOVING from one side to other
        if self.dirnx == -1 and self.pos[0] <= 0:
            self.pos = (self.rows - 1, self.pos[1])
        elif self.dirnx == 1 and self.pos[0] >= self.rows - 1:
            self.pos = (0, self.pos[1])
        elif self.dirny == 1 and self.pos[1] >= self.rows - 1:
            self.pos = (self.pos[0], 0)
        elif self.dirny == -1 and self.pos[1] <= 0:
            self.pos = (self.pos[0], self.rows - 1)
        else: self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, pic, head=False):
        dis = self.w // self.rows

        if head:
            surface.blit(pic, (self.pos[0]*dis, self.pos[1]*dis))
        else:
            surface.blit(self.pic, (self.pos[0] * dis, self.pos[1] * dis))



        ''' dis = self.w // self.rows
        i = self.pos[0] #row
        j = self.pos[1] #column

        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-1, dis-1)) # +1 and -1 to not overdraw white lines
        if head: #draw head
            centre = dis/2
            radius = 3
            circleMiddle = (int(i*dis+centre-radius),int(j*dis+8))
            circleMiddle2 = (int(i * dis + dis - radius*2), int(j * dis + 8))
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius)
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)'''
