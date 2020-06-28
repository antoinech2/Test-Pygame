#Initialisation des modules
import pygame
import threading
import time
import random
pygame.init()

#Initialisations des variables
size = fen_width, fen_height = 1500, 1000
ball_coords = x_ball, y_ball = 250, 250
rhino_coords = x_rhino, y_rhino = random.randint(0, fen_width), random.randint(0, fen_height)
ball_speed = 3
rhino_speed = 1
color = 255, 255, 255
move = x_move, y_move = 0, 0
game_over = False
current_fps = 0
past_fps = 0
timing = pygame.time.Clock()

#Initialisation des ressources
ball = pygame.image.load("ball.png")
rhino = pygame.image.load("rhino.jpg")

#Initialisation de la fenêtre
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ballon chat")

#Fonction de calcul des fps
def calc_fps():
	global past_fps
	global current_fps
	#print(current_fps, "fps")
	past_fps = current_fps
	current_fps = 0
	if not game_over:
		timer = threading.Timer(1.0, calc_fps)
		timer.start()

#Fonction de pause du jeu
def ResumeGame():
	for event in pygame.event.get([pygame.KEYDOWN, pygame.QUIT]):
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		elif event.type == pygame.KEYDOWN:
			return event.key
	return None

calc_fps()

#Fonction d'affichage d'un texte à l'écran
def ShowMessage(texte, taille, police, couleur, x_coord, y_coord):
	TextPoliceInfo = pygame.font.SysFont(police, taille)
	TextMessage = TextPoliceInfo.render(texte, True, pygame.Color(couleur))
	TexteRectangle = TextMessage.get_rect()
	TexteRectangle.center = x_coord, y_coord
	screen.blit(TextMessage, TexteRectangle)
	pygame.display.update()

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
	x_rhino, y_rhino = x_rhino+rhino_speed, y_rhino+rhino_speed
	if not (y_ball+y_move <= 0 or y_ball+y_move >= fen_height-80):
		y_ball += y_move
	if not (x_ball+x_move <= 0 or x_ball+x_move >= fen_width-80):
		x_ball += x_move

	screen.fill(color)
	screen.blit(ball, (x_ball,y_ball))
	screen.blit(rhino, (x_rhino, y_rhino))
	ShowMessage(("Fps:"+str(past_fps)), 20, "arial", "blue", 40, 20)
	pygame.display.flip()

	current_fps+=1

pygame.quit()
quit()
