import sys, os
sys.path.append(os.path.abspath('C:/Users/16479/Documents/GitHub/2D-Physics-Engine'))
sys.path.append(os.path.abspath('C:/Users/16479/Documents/GitHub/2D-Physics-Engine/primitives'))
import pygame
from RigidBodyRectangle import RigidBodyRect
from vec2 import Vec2

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

fps = 60 
'''
# 3-body collision at the same time 
box_1 = RigidBodyRect(400, 950, 100, 100, 100, Vec2(200, 0))
box_2 = RigidBodyRect(800, 950, 100, 100, 100, Vec2(0, 0)) 
box_3 = RigidBodyRect(1200, 950, 100, 100, 100, Vec2(-200, 0)) 
boxes = [box_1, box_2, box_3]
'''

''' # Multiple box scenario 

box_1 = RigidBodyRect(250, 700, 100, 100, 320, Vec2(210, 0))
box_2 = RigidBodyRect(900, 700, 100, 100, 200, Vec2(0, 0)) 
box_3 = RigidBodyRect(1200, 700, 100, 100, 170, Vec2(-150, 0)) 
box_4 = RigidBodyRect(1400, 700, 100, 100, 120, Vec2(-100, 0)) 

boxes = [box_1, box_2, box_3, box_4]
'''
'''
box_1 = RigidBodyRect(600, 100, 100, 100, 100, Vec2(0, 100), 320)
box_2 = RigidBodyRect(900, 900, 100, 100, 100, Vec2(-100, -200)) 

boxes = [box_1, box_2]
'''
colour = (0, 0, 0)

while True: 
	pygame.time.Clock().tick(fps)
	
	for event in pygame.event.get(): 
		if(event.type == pygame.KEYDOWN):
			if(event.key == pygame.K_ESCAPE): 
				sys.exit(0)

	for i, box in enumerate(boxes):
		for j in range(i+1, len(boxes)):
			if box.checkCollision(boxes[j]):
				boxes[j] = box.resolveCollision(boxes[j]) 
				# print(f"BOX[{i}]: velocity = {box.velocity}")
				# print(f"BOX[{j}]: velocity = {boxes[j].velocity}")
	for i, box in enumerate(boxes):
		# print(f"The velocity of box {i} is {box.velocity.x}")
		box.position.x += 1/60 * box.velocity.x 
		box.position.y += 1/60 * box.velocity.y

	screen.fill((255, 255, 255))

	for box in boxes:
		sprite = pygame.Surface((box.width, box.height))
		sprite.set_colorkey((255, 255, 255))
		sprite.fill((0, 0, 0))
		rotated = pygame.transform.rotate(sprite, -box.angle)
		rect = rotated.get_rect()
		screen.blit(rotated, (box.position.x - rect.width / 2, box.position.y - rect.height / 2))

	pygame.display.update() 	