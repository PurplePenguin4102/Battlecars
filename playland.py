import os
import time
import sys
import pygame as pg
pg.init()
os.chdir('C:\Users\Joey\Documents\\Battlecars')


tile = pg.image.load("testtile.png")
tile2 = pg.image.load('othertile.png')

black = (0,0,0)

maze = pg.image.load("Maze.png")

dummy = pg.image.tostring(tile,'RGB')
dummy2 = pg.image.tostring(tile2,'RGB')
dummy += dummy2

char = pg.image.load("character.png")
char_rect = char.get_rect() 

playfield = pg.image.fromstring(dummy, (600,800), 'RGB')

screen = pg.display.set_mode((600,400))

xpos = 0
ypos = 0

inputs = { "Right": "xpos += -400",
     	   "Left": "xpos += 400",
		   "Up": "ypos += 600",
		   "Down": "ypos += -600"}

while 1:

    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
	else:
		pass

#	keyinput = pg.key.get_pressed()
#	print keyinput
	screen.fill(black)
    screen.blit(maze,(xpos,ypos))
    screen.blit(char,(2,2))
    pg.display.flip()
    time.sleep(1)
    

pg.image.save(playfield, 'playfield.png')


# screen = pg.display.set_mode(resolution)
# screen.fill(black)
# screen.blit(tile,tile2)
# time.sleep(5)


print tile
print tile2 