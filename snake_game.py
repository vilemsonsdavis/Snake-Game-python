import random
import snake, edibles
import pygame
import tkinter as tk
from tkinter import messagebox


def drawGrid(w, rows, surface):

    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill((0,0,0))
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()


def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x, y), positions))) > 0: # checks whether the curr pos is on the snake - avoids puttin snack on snake
            continue #does it again
        else:
            break

    return (x, y)


def message_box(subject, content): #creating message box
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def main():
    global width, height, rows, s, snack
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Snake game by Villy")
    pear = pygame.image.load('pear.png')
    apple = pygame.image.load('apple.png') #TO DO - add lives
    s = snake.Snake((255, 0, 0), (10, 10))
    snack = edibles.Fruit(randomSnack(rows, s), pear)
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = edibles.Fruit(randomSnack(rows, s), pear)

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos, s.body[x+1:])):
                message_box('You lost', 'Your score: ' + str(len(s.body)))
                message_box("You lost!", "Play again...")
                s.reset((10, 10))
                snack = edibles.Fruit(randomSnack(rows, s), pear)
                break

        redrawWindow(win)
    pass


main()