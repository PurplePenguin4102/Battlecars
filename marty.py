import pygame
from martysupport import *

class Marty(object):
	"""the player character"""

	def __init__(self,surface,maze,x,y):

		self.x = x
		self.y = y
		self.surface = surface
		self.dirx = 0
		self.diry = 0
		self.marty = []
		self.maze = maze
		self.speed = 3

		self.wall = 0

	def makemarty(self):

		for i in range(5):
			x_0 = self.x + 2 - i
			for j in range(5):
				y_0 = self.y + 2 - j
				self.marty.append((x_0,y_0))

	def movemarty(self):
		
		self.x += self.dirx
		self.y += self.diry

		
		crashtest = [(self.x + 3,self.y),(self.x - 3,self.y),
					 (self.x,self.y + 3),(self.x,self.y - 3)]

		for pix in crashtest:

			r,g,b,a = self.maze.get_at(pix)
			if (r,g,b) != (255,255,255):
				
				self.dirx,self.diry = 0,0
				self.wall = 1

	def key_event(self,event):

		testright = [(self.x + 3,self.y),(self.x + 2,self.y), (self.x+1,self.y)]
		testleft = [(self.x - 3,self.y),(self.x - 2,self.y), (self.x-1,self.y)] 
		testdown = [(self.x,self.y + 3),(self.x,self.y + 2), (self.x,self.y + 1)]  
		testup = [(self.x,self.y - 3),(self.x,self.y - 2), (self.x,self.y - 1)] 
		
		dirlist = [testright,testleft,testdown,testup]

		testpixels = []
		store = []
		for pixlist in dirlist:
			for pix in pixlist:
				r,g,b,a = self.maze.get_at(pix)
				testpixels.append((r,g,b))
			pixlist = zip(pixlist,testpixels)
			store.append(pixlist)
			testpixels = []

		testright,testleft,testdown,testup = store

		
		
		for pix in testdown:		
			if pix[1] == (0,0,0):
				martycommands[pygame.K_DOWN] = '(0,0)'
			else:
				martycommands[pygame.K_DOWN] = '(0,self.speed)'

		for pix in testup:
			if pix[1] == (0,0,0):
				martycommands[pygame.K_UP] = '(0,0)'
			else:
				martycommands[pygame.K_UP] = '(0,-self.speed)'

		for pix in testleft:
			if pix[1] == (0,0,0):
				martycommands[pygame.K_LEFT] = '(0,0)'
			else:
				martycommands[pygame.K_LEFT] = '(-self.speed,0)'

		for pix in testright:
			if pix[1] == (0,0,0):
				martycommands[pygame.K_RIGHT] = '(0,0)'
			else:
				martycommands[pygame.K_RIGHT] = '(self.speed,0)'


		if event.key in martycommands:
			(self.dirx,self.diry) = eval(martycommands[event.key])

	def stopmarty(self):

		self.dirx = 0
		self.diry = 0

	def drawmarty(self):

		for pix in self.marty:
			self.surface.set_at(pix,colours['red'])
		self.marty = []

class Maze(object):

	def __init__(self,surface):
		self.surface = surface
		self.walls = []

	def getwalls(self):
		width = self.surface.get_width()
		height = self.surface.get_height()
		l = []
		for i in range(width):
			for k in range(height):
				l.append((i,k))
		
		for pix in l:
			r,g,b,a = self.surface.get_at(pix)
			if (r,g,b) == (0,0,0):
				self.walls.append(pix)
				
# maze = pygame.image.load('maze.png')
# M = Maze(maze)
# M.getwalls()
#screen = pygame.display.set_mode((640,480))
#m = Marty(screen,screen,7,7)
#m.makemarty()
#m.movemarty()