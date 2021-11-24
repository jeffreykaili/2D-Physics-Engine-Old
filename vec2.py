import math 

# 2D vector class used for the 2D physics engine 

class Vec2: 
	def __init__(self, x, y):
		self.x, self.y = x, y

	def __str__(self):
		return '({}, {})'.format(self.x, self.y)

	def length(self): 
		return math.sqrt(self.x ** 2 + self.y ** 2)

	def __neg__(self): # negation 
		return Vec2(-self.x, -self.y)

	def __add__(self, vec):
		return Vec2(self.x + vec.x, self.y + vec.y)

	def __sub__(self, vec): 
		return self.__add__(-vec)

	def __mul__(self, s): # scalar 
		if(isinstance(s, int) or isinstance(s, float)):
			return Vec2(self.x * s, self.y * s)
		raise NotImplementedError('Can only multiply 2D vector by scalar')

	def __rmul__(self, s):
		return self.__mul__(s)

	def dot(self, vec):
		if(isinstance(vec, Vec2)):
			return self.x * vec.x + self.y * vec.y
		raise NotImplementedError('Dot product should be between two vectors')

	def normalize(self):
		magnitude = self.length() 
		new_vec = Vec2(self.x / magnitude, self.y / magnitude)
		self.x = new_vec.x
		self.y = new_vec.y
		return Vec2(self.x, self.y)

	def perpendicular_vec(self):
		return Vec2(-self.x, self.y)

	def rotate(self, angle):
		angle = math.radians(angle)
		a_cos, a_sin = math.cos(angle), math.sin(angle)
		x = a_cos * self.x - a_sin * self.y 
		y = a_sin * self.x + a_cos * self.y 
		return Vec2(x, y)
