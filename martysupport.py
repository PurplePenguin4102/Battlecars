import pygame

colours = {'blue' : (0,0,255),
	 	   'black' : (0,0,0),
	 	   'white' : (255,255,255),
	 	   'red' : (255,0,0),
	 	   'green' : (0,255,0),
	 	   'cyan' : (0,255,255)}

martycommands = {pygame.K_UP : '(0,-self.speed)',
	 			 pygame.K_DOWN : '(0,self.speed)',
				 pygame.K_LEFT : '(-self.speed,0)',
				 pygame.K_RIGHT : '(self.speed,0)', }