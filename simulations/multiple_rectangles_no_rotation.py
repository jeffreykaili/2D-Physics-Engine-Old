import sys, os
sys.path.append(os.path.abspath('C:/Users/16479/Documents/GitHub/2D-Physics-Engine'))
sys.path.append(os.path.abspath('C:/Users/16479/Documents/GitHub/2D-Physics-Engine/primitives'))
import pygame
from RigidBodyRectangle import RigidBodyRect
from vec2 import Vec2

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

fps = 60 
box_1 = RigidBodyRect(300, 950, 100, 100, 100, Vec2(60, 0))
box_2 = RigidBodyRect(1000, 950, 100, 100, 100, Vec2(-50, 0)) 
box_3 = RigidBodyRect(1700, 950, 100, 100, 100, Vec2(-100, 0)) 
boxes = [box_1, box_2, box_3]

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

	for box in boxes:
		box.position.x += 1/60 * box.velocity.x 

	screen.fill((255, 255, 255))

	for box in boxes:
		pygame.draw.rect(screen, colour, pygame.Rect(box.position.x, box.position.y, box.width, box.height))

	pygame.display.update() 	