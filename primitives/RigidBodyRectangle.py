import sys, os
sys.path.append(os.path.abspath('C:/Users/16479/Documents/GitHub/2D-Physics-Engine'))
from vec2 import Vec2
from AABB import AABB 
import pygame

class RigidBodyRect:
	def __init__(self, x, y, width, height, mass, velocity = Vec2(0, 0), restitution = 1): 
		self.position = Vec2(x, y)
		self.width = width 
		self.height = height 
		self.mass = mass 
		self.invmass = 1 / mass 
		self.velocity = velocity
		self.restitution = restitution 
		self.sprite = pygame.Surface((width, height))
		self.sprite.set_colorkey((0, 0, 0))
		self.sprite.fill((0, 0, 0))

	def checkCollision(self, B):
		first = AABB(Vec2(self.position.x, self.position.y - self.height), Vec2(self.position.x + self.width, self.position.y))
		second = AABB(Vec2(B.position.x, B.position.y - B.height), Vec2(B.position.x + B.width, B.position.y))
		return first.isCollideAABB(second)

	def resolveCollision(self, B):
		rv = B.velocity - self.velocity

		normal = B.position - self.position
		normal.normalize() 
		velocity_along_normal = rv.dot(normal)

		if velocity_along_normal > 0: 
			return B

		e = min(self.restitution, B.restitution)
		print(velocity_along_normal)
		j = -(1 + e) * velocity_along_normal
		j /= self.invmass + B.invmass

		impulse = j * normal
		print(f"IMPULSE IS: {impulse}")
		self.velocity -= self.invmass * impulse
		B.velocity += B.invmass * impulse 
		self.position.x += 1/1e10 * self.velocity.x


		print(f"B IS AT: {B.position} WITH VELOCITY: {B.velocity}")
		return B