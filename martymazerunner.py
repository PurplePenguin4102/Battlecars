import pygame
from marty2 import Marty

pygame.init
maze = pygame.image.load('Maze.png')

width = 640
height = 480

screen = pygame.display.set_mode((width,height))

m = Marty(screen, maze, 7,7)

running = True
while running:

	screen.blit(maze,(0,0))
	pygame.draw.rect(maze, (255,200,0), m.rect)
	

	event = pygame.event.poll()

	if event.type == pygame.QUIT:
		running = False
	if event.type == pygame.KEYUP:
		m.stopmarty()
	if event.type == pygame.KEYDOWN:
		m.key_event(event)
	
	

	

	pygame.display.flip()