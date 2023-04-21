import pygame
import time

class Object():
	pass
		
transition = False
transition_data = False

inited = False

def init(transition):
	pass 

def init(i_screen, i_window_width, i_window_height, i_background_color = [0, 0, 0]):
	global screen, window_width, window_height, background_color, inited
	screen = i_screen
	window_width = i_window_width
	window_height = i_window_height
	background_color = i_background_color
	inited = True
	
def run(name, duration = 1, x = -1, y = -1):
	global transition, transition_data
	if inited == False:
		raise Exception("You must init transitions before using it!")
	transition = name
	transition_data = Object()
	transition_data.duration = duration
	transition_data.start = time.clock()
	transition_data.screen = screen.copy()
	transition_data.current_screen = False
	transition_data.x = x
	transition_data.y = y
	
def updateScreen():
	global transition, transition_data
	if inited == False:
		raise Exception("You must init transitions before using it!")
	if transition != False:
		current_time = time.clock()
		time_ratio = (current_time - transition_data.start) / transition_data.duration
		if time_ratio > 1.0:
			transition_data = False
			transition = False
		else:
			screen.fill(background_color)
			if transition == "fadeOutUp":
				transition_data.screen.set_alpha(255-255*time_ratio)
				rect1 = transition_data.screen.get_rect()
				transition_data.current_screen = pygame.transform.smoothscale(transition_data.screen, [int(rect1[2]*(1+time_ratio)), int(rect1[3]*(1+time_ratio))])
				transition_data.current_screen = pygame.transform.rotate(transition_data.current_screen, 10*time_ratio)
			elif transition == "fadeOutDown":
				transition_data.screen.set_alpha(255-255*time_ratio)
				rect1 = transition_data.screen.get_rect()
				transition_data.current_screen = pygame.transform.smoothscale(transition_data.screen, [int(rect1[2]*(1-time_ratio)), int(rect1[3]*(1-time_ratio))])
			rect2 = transition_data.current_screen.get_rect()
			if transition_data.x != -1:
				x = (rect2[2]*transition_data.x)/window_width
			else:
				x = rect2[2]/2
			if transition_data.y != -1:
				y = (rect2[3]*transition_data.y)/window_height
			else:
				y = rect2[3]/2
			screen.blit(transition_data.current_screen, [window_width/2-x, window_height/2-y])
	return transition