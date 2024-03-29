import sys, os
sys.path.append(os.path.abspath('C:/Users/16479/Documents/GitHub/2D-Physics-Engine'))
from vec2 import Vec2

class AABB:
	def __init__(self, mi, mx):
		if(isinstance(mi, Vec2) and isinstance(mx, Vec2)):
			self.mi = mi # mi --> lower x and y points (top left)
			self.mx = mx # mx --> upper x and y points (bottom right)
		else:
			raise NotImplementedError('Must pass in two vectors for Axis Aligned Bounding Box')

	def __str__(self):
		return '({}, {}) | ({}, {})'.format(self.mi.x, self.mi.y, self.mx.x, self.mx.y)

	def isCollideAABB(self, AABB2):
		if(isinstance(AABB2, AABB)):
			if(self.mx.x < AABB2.mi.x or self.mi.x > AABB2.mx.x
			or self.mx.y < AABB2.mi.y or self.mi.y > AABB2.mx.y):
				return False 
			return True 
		return NotImplementedError('Must pass in another AABB to check for contact.')

if __name__ == '__main__':
	print(AABB(Vec2(1, 1), Vec2(2, 2)).isCollideAABB(AABB(Vec2(1.9, 2), Vec2(3, 3))))