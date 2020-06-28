#Initialisation des modules
import pygame
import threading
import time
import random
from datetime import datetime
pygame.init()

#Initialisations des variables
size = fen_width, fen_height = 1500, 1000
ball_coords = x_ball, y_ball = 250, 250
ball_speed = 5 #pixels/ticks
color = 255, 255, 255
move = x_move, y_move = 0, 0
game_over = False
current_fps, past_fps, current_tps, past_tps = 0, 0, 0, 0
timing = pygame.time.Clock()
tick_per_second = 50
tick_sleep = 1/tick_per_second

number_balls = 2000
ball = []
for i in range (number_balls):
	ball.append([random.randint(0, fen_width), random.randint(0, fen_height)])

#print(ball[1][0])

#Initialisation des ressources
ball_image = pygame.image.load("ball.png")

#Initialisation de la fenêtre
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ballon chat")

#Fonction de calcul des fps
def calc_fps():
	global past_fps, current_fps, past_tps, current_tps
	past_fps = current_fps
	past_tps = current_tps
	current_fps, current_tps = 0, 0
	if not game_over:
		timer_fps = threading.Timer(1.0, calc_fps)
		timer_fps.start()

#Fonction de pause du jeu
def ResumeGame():
	for event in pygame.event.get([pygame.KEYDOWN, pygame.QUIT]):
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		elif event.type == pygame.KEYDOWN:
			return event.key
	return None

#Fonction d'affichage d'un texte à l'écran
def ShowMessage(texte, taille, police, couleur, x_coord, y_coord):
	TextPoliceInfo = pygame.font.SysFont(police, taille)
	TextMessage = TextPoliceInfo.render(texte, True, pygame.Color(couleur))
	TexteRectangle = TextMessage.get_rect()
	TexteRectangle.center = x_coord, y_coord
	screen.blit(TextMessage, TexteRectangle)
	#pygame.display.update()

#Fonction principale de calcul
def CalcTick():
	global game_over, x_move, y_move, x_ball, y_ball, current_tps
	if not (y_ball+y_move <= 0 or y_ball+y_move >= fen_height-80):
		y_ball += y_move
	if not (x_ball+x_move <= 0 or x_ball+x_move >= fen_width-80):
		x_ball += x_move

	for i in range (number_balls):
		ball[i]=(ball[i][0]+x_move, ball[i][1]+y_move)

	current_tps+=1


def DoTick():
	global current_tps
	#if not game_over:
	#	timer_tick = threading.Timer(1, DoTick)
	#	timer_tick.start()
	#for i in range (tick_per_second):
	while not game_over:
		next_tick = datetime.timestamp(datetime.now()) + tick_sleep
		CalcTick()
		#while datetime.timestamp(datetime.now()) < next_tick:
		#	timing.tick()
		time.sleep(next_tick-datetime.timestamp(datetime.now()))

calc_fps()
#DoTick()
timer_tick = threading.Timer(0.1, DoTick)
timer_tick.start()


#Boucle principale
while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				y_move = -ball_speed
			elif event.key == pygame.K_DOWN:
				y_move = ball_speed
			elif event.key == pygame.K_RIGHT:
				x_move = ball_speed
			elif event.key == pygame.K_LEFT:
				x_move = -ball_speed
			elif event.key == pygame.K_p:
				ShowMessage("Jeu en pause", 100, "arial", "red", 500, 200)
				ShowMessage("Appuyez sur une touche pour continuer...", 20, "arial", "red", 500, 300)
				while ResumeGame() == None:
					timing.tick()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				y_move = 0
			elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
				x_move = 0
		elif event.type == pygame.VIDEORESIZE:
			pygame.display.set_mode(event.size)

	screen.fill(color)
	for i in range (number_balls):
		screen.blit(ball_image, (ball[i]))
	screen.blit(ball_image, (x_ball,y_ball))
	ShowMessage(("Fps:"+str(past_fps)+" ,TPS:"+str(past_tps)), 20, "arial", "blue", 80, 20)
	#print(past_fps, past_tps)
	pygame.display.flip()
	current_fps+=1

pygame.quit()
quit()
