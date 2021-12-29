import sys, os, copy
sys.path.append(os.path.abspath('C:/Users/16479/Documents/GitHub/2D-Physics-Engine'))
sys.path.append(os.path.abspath('C:/Users/16479/Documents/GitHub/2D-Physics-Engine/primitives'))
import pygame
from RigidBodyRectangle import RigidBodyRect
from vec2 import Vec2

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

fps = 60 
ground = RigidBodyRect(960, 890, 1920, 380, 0, Vec2(0, 0), 0, 0) 
box1 = RigidBodyRect(960, 600, 100, 100, 10, Vec2(100, 100))
boxes = [ground, box1]
gravity_a = 10  

def PositionalCorrection(A, B, dep, normal):
    percent = 0.8
    correction = dep / (A.invmass + B.invmass) * percent * normal 
    print("CORRECTION:",correction)
    A.position += A.invmass * correction 
    B.position -= B.invmass * correction
    return (A, B)

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
                boxes[i], boxes[j] = PositionalCorrection(boxes[i], boxes[j], res[1], res[2])
                print(boxes[i].velocity.x, boxes[j].velocity.x)

    for i, box in enumerate(boxes):
        if(box.mass):
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