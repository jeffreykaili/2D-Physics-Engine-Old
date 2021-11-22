import sys, os
sys.path.append(os.path.abspath('C:/Users/16479/Documents/GitHub/2D-Physics-Engine'))
from vec2 import Vec2

class Particle:
	def __init__(self, position, velocity, mass):
		self.position = position 
		self.velocity = velocity 
		self.mass = mass 

	def __str__(self):
		return '({}, {}) | ({}, {}) | {}'.format(self.position.x, self.position.y, self.velocity.x, self.velocity.y, self.mass)