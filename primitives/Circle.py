import sys, os
sys.path.append(os.path.abspath('C:/Users/16479/Documents/GitHub/2D-Physics-Engine'))
from vec2 import Vec2

class Circle:
	def __init__(self, position, radius):
		self.radius = radius 
		self.position = position 

	def __str__(self):
		return 'Center at ({}, {}) with radius {}'.format(self.position.x, self.position.y, self.radius)

	def isCollideCircle(self, C2):
		if(isinstance(C2, Circle)):
			r = self.radius + C2.radius 
			r *= r 
			return r > ((self.position.x + C2.position.x)**2 + (self.position.y + C2.position.y)**2)
		raise NotImplementedError('Must pass in another circle to check for contact.')
