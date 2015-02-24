import pygame
from martysupport import *

class Marty(object):
	"""the player character"""

	def __init__(self,surface,maze,x,y):

		self.rect = pygame.Rect(7,7,3,3)

	def movemarty(self):
		pass