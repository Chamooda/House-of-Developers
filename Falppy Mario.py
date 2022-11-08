# Import module
import random
import input_inp
import sys
import pygame
from pygame.locals import *
import hashlib
from PIL import Image
import HackathonEncrypt
import HackatonImageGenerator
import mysql.connector
import HashToIMG

num=HackatonImageGenerator.kitne_user()
# HashToIMG.Hash_Assignment(num)
imgName = HackatonImageGenerator.ImgGenerator(num)

hash1 = HackathonEncrypt.Encrypt(imgName)
#HashToIMG.Hash_To_IMAGE(hash1)

#This module is used to get the user id and password, to complete the login process
cred=input_inp.inp()
#xusername = input("Re-Enter username to confirm avatars : ")
name=cred[0]
log=cred[1]
comp=cred[2]
compare=cred[3]
if log=='Login Successful':
	print("Login Successful, have a fun time !")
	pass
else:
	print("Invald credentials, please try again !")
	sys.exit()


# Declaring the dimensions of the game window
window_width = 600
window_height = 499

# set height and width of window
window = pygame.display.set_mode((window_width, window_height))
elevation = window_height * 0.8
game_images = {}                                 #Empty dictionary that will store the game assets
framepersecond = 32
pipeimage = 'images/pipe2.png'
background_image = 'images/bg4.jpg'
birdplayer_image = 'images/bird.png'             #Getting the game assets
sealevel_image = 'images/base2.png'
# mix_img = ["background base2 pipe","bg4 base2 pipe4","bg5 base5 pipe3","bg6 base6 pipe6"]
# used_img = mix_img[random.randint(0,3)]
# xxpipe = used_img[2]
# xxbase = used_img[1]
# xxbg = used_img[0]


# pipeimage = 'images/'+f"{xxpipe}"+'.png'
# background_image = 'images/'+f"{xxbase}"+'.jpg'
# sealevel_image = 'images/base2'+f"{xxbg}"+'.png'


# mydb=mysql.connector.connect(
# host="localhost",
# user="root",
# password="tiger"
# )
# mycursor = mydb.cursor()
# mycursor.execute("use test1")
# sql20="select hash from flappy_bird where user_id =%s"
# val20=(xusername,)
# mycursor.execute(sql20,val20)
# xlist = mycursor.fetchone()[0][0].split()
# xvalue = xlist[0]

# mycursor.execute("use test1")
# sql21="select name from hash_image where hash =%s"
# val21=(xvalue,)
# mycursor.execute(sql21,val21)
# xmane = mycursor.fetchone()
# print(xmane)


# HashToIMG.Hash_To_IMAGE(xvalue)


# birdplayer_image = 'images/'+f'{xmane}'+'.png'             #Getting the game assets
lscore=[1,2,0]

#This is the main game function
def flappygame():

	#Initializing the coordinates
	Your_score = 0
	horizontal = int(window_width/5)
	vertical = int(window_width/2)
	ground = 0
	mytempheight = 100

	# Generating two pipes for blitting on window
	first_pipe = createPipe()
	second_pipe = createPipe()

	down_pipes = [
		{'x': window_width+300-mytempheight,
		'y': first_pipe[1]['y']},
		{'x': window_width+300-mytempheight+(window_width/2),
		'y': second_pipe[1]['y']},
	]

	up_pipes = [
		{'x': window_width+300-mytempheight,
		'y': first_pipe[0]['y']},
		{'x': window_width+200-mytempheight+(window_width/2),
		'y': second_pipe[0]['y']},
	]
	#Only two pipes are generated at any instance in the game

	#Horizontal pipe velocity
	pipeVelX = -4

	bird_velocity_y = -9                        #Initial velocity of the bird
	bird_Max_Vel_Y = 10
	bird_Min_Vel_Y = -8
	birdAccY = 1

	bird_flap_velocity = -8                     #Velocity of the bird while flapping
	bird_flapped = False
	while True:

		#Handling the key inputs
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
				if vertical > 0:
					bird_velocity_y = bird_flap_velocity
					bird_flapped = True

		# This function will return true if the flappybird is crashed
		game_over = isGameOver(horizontal,
							vertical,
							up_pipes,
							down_pipes)
		if game_over:
			return

		#Checking for the score
		playerMidPos = horizontal + game_images['flappybird'].get_width()/2
		for pipe in up_pipes:
			pipeMidPos = pipe['x'] + game_images['pipeimage'][0].get_width()/2
			if pipeMidPos <= playerMidPos < pipeMidPos + 4:
				Your_score += 1
				lscore.append(Your_score)
				print(f"Your_score is {Your_score}")
				

		#Now we adjust the velocity to increase the game difficulty
		if bird_velocity_y < bird_Max_Vel_Y and not bird_flapped:
			bird_velocity_y += birdAccY

		if bird_flapped:
			bird_flapped = False
		playerHeight = game_images['flappybird'].get_height()
		vertical = vertical + \
			min(bird_velocity_y, elevation - vertical - playerHeight)

		# Moving pipes to the left
		for upperPipe, lowerPipe in zip(up_pipes, down_pipes):
			upperPipe['x'] += pipeVelX
			lowerPipe['x'] += pipeVelX

		#We add a new pipe when the last one is about to move out of screen
		if 0 < up_pipes[0]['x'] < 5:
			newpipe = createPipe()
			up_pipes.append(newpipe[0])
			down_pipes.append(newpipe[1])

		#Removing pipes which are out of the screen
		if up_pipes[0]['x'] < -game_images['pipeimage'][0].get_width():
			up_pipes.pop(0)
			down_pipes.pop(0)

		# Lets blit our game images now
		window.blit(game_images['background'], (0, 0))
		for upperPipe, lowerPipe in zip(up_pipes, down_pipes):
			window.blit(game_images['pipeimage'][0],
						(upperPipe['x'], upperPipe['y']))
			window.blit(game_images['pipeimage'][1],
						(lowerPipe['x'], lowerPipe['y']))

		window.blit(game_images['sea_level'], (ground, elevation))
		window.blit(game_images['flappybird'], (horizontal, vertical))

		# Fetching the digits of score.
		numbers = [int(x) for x in list(str(Your_score))]
		width = 0

		# finding the width of score images from numbers.
		for num in numbers:
			width += game_images['scoreimages'][num].get_width()
		Xoffset = (window_width - width)/1.1

		# Blitting the images on the window.
		for num in numbers:
			window.blit(game_images['scoreimages'][num],
						(Xoffset, window_width*0.02))
			Xoffset += game_images['scoreimages'][num].get_width()

		# Refreshing the game window and displaying the score.
		pygame.display.update()
		framepersecond_clock.tick(framepersecond)

#This function will check for the gameover condition
def isGameOver(horizontal, vertical, up_pipes, down_pipes):
	
	#Checking if the bird hits the sea or flies too high
	if vertical > elevation - 25 or vertical < 0:
		fscore=lscore[-1]
		input_inp.score(name,fscore)
		input_inp.winner(name,fscore,comp,compare)
		return True

	#CHecking if the bird hits the upper pipes
	for pipe in up_pipes:
		pipeHeight = game_images['pipeimage'][0].get_height()
		if(vertical < pipeHeight + pipe['y'] and\
		abs(horizontal - pipe['x']) < game_images['pipeimage'][0].get_width()):
			fscore=lscore[-1]
			input_inp.score(name,fscore)
			input_inp.winner(name,fscore,comp,compare)
			return True

	#Checking if the bird hits the lower pipes
	for pipe in down_pipes:
		if (vertical + game_images['flappybird'].get_height() > pipe['y']) and\
		abs(horizontal - pipe['x']) < game_images['pipeimage'][0].get_width():
			fscore=lscore[-1]
			input_inp.score(name,fscore)
			input_inp.winner(name,fscore,comp,compare)
			return True
	return False

#This function will generate pipes of random heights
def createPipe():
	offset = window_height/3
	#THis is the area between the pipes, i.e. 1/3rd of the screen will be fixed for movement of birs
	pipeHeight = game_images['pipeimage'][0].get_height()

	#Now we generate pipes of random heights
	y2 = offset + \
		random.randrange(
			0, int(window_height - game_images['sea_level'].get_height() - 1.2 * offset))
	pipeX = window_width + 10
	y1 = pipeHeight - y2 + offset

	#Now from the above random generated values, we create a range of pipe heights
	pipe = [
		# upper Pipe
		{'x': pipeX, 'y': -y1},

		# lower Pipe
		{'x': pipeX, 'y': y2}
	]
	return pipe

# program where the game starts
if __name__ == "__main__":

	pygame.init()                                               #Initializes the game application
	framepersecond_clock = pygame.time.Clock()                  #Used to alter the speed of the bird

	pygame.display.set_caption('Flappy Bird Game')              #Title of the game
	
	game_images['scoreimages'] = (                              #Loaading all game assets in a list
		pygame.image.load('images/0.png').convert_alpha(),
		pygame.image.load('images/1.png').convert_alpha(),
		pygame.image.load('images/2.png').convert_alpha(),
		pygame.image.load('images/3.png').convert_alpha(),
		pygame.image.load('images/4.png').convert_alpha(),
		pygame.image.load('images/5.png').convert_alpha(),
		pygame.image.load('images/6.png').convert_alpha(),
		pygame.image.load('images/7.png').convert_alpha(),
		pygame.image.load('images/8.png').convert_alpha(),
		pygame.image.load('images/9.png').convert_alpha()
	)
	game_images['flappybird'] = pygame.image.load(
		birdplayer_image).convert_alpha()
	game_images['sea_level'] = pygame.image.load(
		sealevel_image).convert_alpha()
	game_images['background'] = pygame.image.load(
		background_image).convert_alpha()
	game_images['pipeimage'] = (pygame.transform.rotate(pygame.image.load(
		pipeimage).convert_alpha(), 180), pygame.image.load(
	pipeimage).convert_alpha())

	print("WELCOME TO THE FLAPPY BIRD GAME")
	print("Press space or enter to start the game")

	# Here starts the main game

	while True:

		# sets the coordinates of flappy bird

		horizontal = int(window_width/5)
		vertical = int(
			(window_height - game_images['flappybird'].get_height())/2)
		ground = 0
		while True:
			for event in pygame.event.get():

				# if user clicks on cross button, close the game
				if event.type == QUIT or (event.type == KEYDOWN and \
										event.key == K_ESCAPE):
					pygame.quit()
					sys.exit()

				# If the user presses space or
				# up key, start the game for them
				elif event.type == KEYDOWN and (event.key == K_SPACE or\
												event.key == K_UP):
					flappygame()

				# if user doesn't press anykey Nothing happen
				else:
					window.blit(game_images['background'], (0, 0))
					window.blit(game_images['flappybird'],
								(horizontal, vertical))
					window.blit(game_images['sea_level'], (ground, elevation))
					pygame.display.update()
					framepersecond_clock.tick(framepersecond)

