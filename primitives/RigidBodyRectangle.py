import sys, os
sys.path.append(os.path.abspath('C:/Users/16479/Documents/GitHub/2D-Physics-Engine'))
from vec2 import Vec2
from AABB import AABB 
import pygame

class RigidBodyRect:
	def __init__(self, x, y, width, height, mass, velocity = Vec2(0, 0), angle = 0.0, restitution = 1): 
		self.position = Vec2(x, y)
		self.width = width 
		self.height = height 
		self.mass = mass 
		self.invmass = 1 / mass 
		self.angle = angle
		self.restitution = restitution 

		self.velocity = velocity
		self.angular_velocity = 0

		self.sprite = pygame.Surface((width, height))
		self.sprite.set_colorkey((0, 0, 0))
		self.sprite.fill((0, 0, 0))

	def get_edges(self):
		return [
			Vec2(v[0], v[1]).rotate(self.angle) for v in (
				(self.width, 0),
				(0, self.height),
				(-self.width, 0),
				(0, -self.height),
			)
		]

	def get_vertices(self):
		hw, hh = self.width / 2, self.height / 2
		return [	
			self.position + Vec2(v[0], v[1]).rotate(-self.angle) for v in (
				(-hw, -hh),
				(hw, -hh),
				(hw, hh),
				(-hw, hh)
			)
		]

	def checkCollision(self, B):
		''' # Performs AABB check for objects containing no rotation
		first = AABB(Vec2(self.position.x, self.position.y - self.height), Vec2(self.position.x + self.width, self.position.y))
		second = AABB(Vec2(B.position.x, B.position.y - B.height), Vec2(B.position.x + B.width, B.position.y))
		return first.isCollideAABB(second)
		''' 
		# Otherwise, we use SAT (seperating axis theorem)
		def project_on_axis(axis, vertices):
			projections = [v.dot(axis) for v in vertices]
			return min(projections), max(projections)

		def projection_overlap(AP, BP):
			al, ar = AP
			bl, br = BP 
			return bl <= al <= br or bl <= ar <= br or al <= bl <= ar or al <= br <= ar  

		all_edges = B.get_edges() + self.get_edges()
		perp_edges = [v.perpendicular_vec().normalize() for v in all_edges] # We check along the perpendicular vector to each axis 

		for edge in perp_edges:
			A_projection = project_on_axis(edge, self.get_vertices())
			B_projection = project_on_axis(edge, B.get_vertices())
			if not projection_overlap(A_projection, B_projection): 
				return False 
		print(f"COLLISION DETECTED:\nBOTTOM LEFT IS: {self.position}\nREST OF VERTICES ARE:")
		print(*(self.get_vertices()))
		print(f"OTHER SHAPE:")
		print(*(B.get_vertices()))
		return True


	def resolveCollision(self, B):
		rv = B.velocity - self.velocity

		normal = B.position - self.position
		normal.normalize() 
		velocity_along_normal = rv.dot(normal)

		if velocity_along_normal > 0: 
			return B

		e = min(self.restitution, B.restitution)
		# print(velocity_along_normal)
		j = -(1 + e) * velocity_along_normal
		j /= self.invmass + B.invmass

		impulse = j * normal
		# print(f"IMPULSE IS: {impulse}")
		self.velocity -= self.invmass * impulse
		B.velocity += B.invmass * impulse 

		# print(f"B IS AT: {B.position} WITH VELOCITY: {B.velocity}")
		return B