import sys, os
sys.path.append(os.path.abspath('C:/Users/16479/Documents/GitHub/2D-Physics-Engine'))
sys.path.append(os.path.abspath('C:/Users/16479/Documents/GitHub/2D-Physics-Engine/primitives'))
import pygame
from RigidBodyRectangle import RigidBodyRect
from vec2 import Vec2

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

fps = 60 


box_1 = RigidBodyRect(600, 100, 100, 100, 100, Vec2(-20, 140), 150)
box_2 = RigidBodyRect(900, 900, 100, 100, 100, Vec2(-100, -200), 30) 
box_3 = RigidBodyRect(1000, 200, 100, 100, 100, Vec2(-100, 200), 60) 

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
			res = box.checkCollision(boxes[j])
			if res != False:
				boxes[j] = box.resolveCollision(boxes[j], res[1]) 

	for i, box in enumerate(boxes):
		box.position.x += 1/60 * box.velocity.x 
		box.position.y += 1/60 * box.velocity.y
		box.angular_velocity += box.torque / box.inertia * 1/60
		box.angle += box.angular_velocity * 1/60

	screen.fill((255, 255, 255))

	for box in boxes:
		sprite = pygame.Surface((box.width, box.height))
		sprite.set_colorkey((255, 255, 255))
		sprite.fill((0, 0, 0))
		rotated = pygame.transform.rotate(sprite, -box.angle)
		rect = rotated.get_rect()
		screen.blit(rotated, (box.position.x - rect.width / 2, box.position.y - rect.height / 2))

	pygame.display.update() 	