import pygame
import threading
import time
pygame.init()

size = fen_width, fen_height = 1500, 1000
ball_coords = x_ball, y_ball = 250, 250
speed = 3
color = 255, 255, 255
screen = pygame.display.set_mode(size)
move = x_move, y_move = 0, 0
ball = pygame.image.load("ball.png")
game_over = False
current_fps = 0
timing = pygame.time.Clock()

pygame.display.set_caption("Ballon chat")

def calc_fps():
	global current_fps
	print(current_fps, "fps")
	current_fps = 0
	if not game_over:
		timer = threading.Timer(1.0, calc_fps)
		timer.start()

def ResumeGame():
	for event in pygame.event.get([pygame.KEYDOWN, pygame.QUIT]):
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		elif event.type == pygame.KEYDOWN:
			#print("ok")
			#continue
			return event.key
	return None

calc_fps()

def ShowMessage(texte, taille, police, couleur, x_coord, y_coord):
	TextPoliceInfo = pygame.font.SysFont(police, taille)
	TextMessage = TextPoliceInfo.render(texte, True, pygame.Color(couleur))
	TexteRectangle = TextMessage.get_rect()
	TexteRectangle.center = x_coord, y_coord
	screen.blit(TextMessage, TexteRectangle)
	pygame.display.update()

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				y_move = -speed
			elif event.key == pygame.K_DOWN:
				y_move = speed
			elif event.key == pygame.K_RIGHT:
				x_move = speed
			elif event.key == pygame.K_LEFT:
				x_move = -speed
			elif event.key == pygame.K_p:
				#print ("ok")
				ShowMessage("Jeu en pause", 100, "arial", "red", 500, 200)
				ShowMessage("Appuyez sur une touche pour continuer...", 20, "arial", "red", 500, 300)
				while ResumeGame() == None:
					timing.tick()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				y_move = 0
			elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
				x_move = 0
	#ballrect = ballrect.move(speed)
	#if ballrect.left < 0 or ballrect.right > fen_width:
	#	speed[0] = -speed[0]
	#if ballrect.top < 0 or ballrect.bottom > fen_height:
	#	speed[1] = -speed[1]
	if not (y_ball+y_move <= 0 or y_ball+y_move >= fen_height-80):
		y_ball += y_move
	if not (x_ball+x_move <= 0 or x_ball+x_move >= fen_width-80):
		x_ball += x_move
	#print ("y_ball = ", y_ball, "height = ", fen_height)


	screen.fill(color)
	#ShowMessage("Bonjour!", 100, "arial", "red", 200, 200)
	screen.blit(ball, (x_ball,y_ball))
	pygame.display.flip()


	current_fps+=1

pygame.quit()
quit()
