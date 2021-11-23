import sys, os
sys.path.append(os.path.abspath('C:/Users/16479/Documents/GitHub/2D-Physics-Engine'))
sys.path.append(os.path.abspath('C:/Users/16479/Documents/GitHub/2D-Physics-Engine/primitives'))
import pygame
from RigidBodyRectangle import RigidBodyRect
from vec2 import Vec2

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#screen = pygame.display.set_mode((1919, 1079))

fps = 60 

box_1 = RigidBodyRect(600, 950, 100, 100, 100, Vec2(60, 0))
box_2 = RigidBodyRect(1200, 950, 100, 100, 200, Vec2(-100, 0)) 
colour = (0, 0, 0)

while True: 
	pygame.time.Clock().tick(fps)
	
	for event in pygame.event.get(): 
		if(event.type == pygame.KEYDOWN):
			if(event.key == pygame.K_ESCAPE): 
				sys.exit(0)

	if box_1.checkCollision(box_2):
		colour = (255, 0, 0)
		box_2 = box_1.resolveCollision(box_2)
		print(f"NEW BOX 1 VELOCITY = {box_1.velocity}")
		print(f"NEW BOX 2 VELOCITY = {box_2.velocity}")
	else:
		colour = (0, 0, 0)

	box_1.position.x += 1/60 * box_1.velocity.x
	box_2.position.x += 1/60 * box_2.velocity.x

	screen.fill((255, 255, 255))

	pygame.draw.rect(screen, colour, pygame.Rect(box_1.position.x, box_1.position.y, box_1.width, box_1.height))
	pygame.draw.rect(screen, colour, pygame.Rect(box_2.position.x, box_2.position.y, box_2.width, box_2.height))

	pygame.display.update() 	