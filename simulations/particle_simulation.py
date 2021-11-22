import sys, os
sys.path.append(os.path.abspath('C:/Users/16479/Documents/GitHub/2D-Physics-Engine'))
sys.path.append(os.path.abspath('C:/Users/16479/Documents/GitHub/2D-Physics-Engine/primitives'))
from vec2 import Vec2
from Particle import Particle 
import pygame 
from random import randint

def initializeParticles(N):
	# N is the number of particles  
	particles = []
	for i in range(N):
		p = Particle(Vec2(randint(100, 1800), randint(0, 800)), Vec2(0, 0), 1)
		particles.append(p)
	return particles 

def calcForces(p):
	return Vec2(0, p.mass * 9.81)

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
fps = 60 
particles = initializeParticles(10)

while True: 
	pygame.time.Clock().tick(fps)
	
	for event in pygame.event.get(): 
		if(event.type == pygame.KEYDOWN):
			if(event.key == pygame.K_ESCAPE): 
				sys.exit(0)
	screen.fill((255, 255, 255))
	for particle in particles:
		force = calcForces(particle)
		acceleration = Vec2(force.x / particle.mass, force.y / particle.mass)
		particle.velocity.x += acceleration.x * 1/60 
		particle.velocity.y += acceleration.y * 1/60 
		particle.position.x += particle.velocity.x * 1/60 
		particle.position.y += particle.velocity.y * 1/60 
		pygame.draw.circle(screen, (0, 0, 0), (particle.position.x, particle.position.y), 10)
	
	pygame.display.update() 	