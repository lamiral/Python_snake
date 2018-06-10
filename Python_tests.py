import pygame
from pygame.locals import *

#---------------- Utils ----------------------

def swap(a,b):
	a,b = b,a

#---------------- Class window ----------------------

class Window:
	w = 0
	h = 0

	screen = None

	def __init__(self,_w,_h):
		self.w = _w
		self.h = _h
		self.screen = pygame.display.set_mode((self.w,self.h),0,32)

	def get_window(self):
		return self.screen

	def info(self):
		print("[*]Window info: Width = " + str(self.w) + " Height = " + str(self.h))

#---------------- Class My_Rect ----------------------

class My_Rect:
	w,h,x,y = 0,0,0,0
	color = 0

	_Rect = None

	def __init__(self,_w,_h,_x,_y,_color):
		self.w,self.h,self.x,self.y = _w,_h,_x,_y
		self.color = _color

		self._Rect = Rect((self.x,self.y),(self.w,self.h))

	def draw_rect(self,screen):
		pygame.draw.rect(screen,self.color,self._Rect,0)

	def info(self):
		print("[*]Rect info : X = " + str(self.x) + " Y = " + str(self.y))

	def change(self):
		self._Rect = Rect((self.x,self.y),(self.w,self.h))

#---------------- Class Field ----------------------

class Field:

	w = 0
	h = 0
	color = None

	def __init__(self,_w,_h,_color):
		self.w = _w
		self.h = _h
		self.color = _color

	def draw_field(self,screen,step):
		for i in range(0,self.w,step):
			pygame.draw.line(screen,self.color,(i,0),(i,self.h),3)
		for i in range(0,self.h,step):
			pygame.draw.line(screen,self.color,(i,0),(i,self.w),3)


#---------------- Class Snake ----------------------

class Snake:

	snake = []

	color = 0

	x,y = 0,0
	w,h = 0,0

	width,height = 0,0

	_dir = 0

	def __init__(self,_x,_y,_w,_h,wd,hg):

		self.color = [255,0,0]

		self.x = _x
		self.y = _y
		self.w = _w
		self.h = _h

		self.width = wd
		self.height = hg


		for i in range(4):
			self.snake.append(My_Rect(self.w,self.h,_x + (self.w*i),_y,self.color))


	def draw_snake(self,screen):
		for rect in self.snake:
			rect.draw_rect(screen)

	def move(self):

		i = len(self.snake) - 1

		while i > 0:

			self.snake[i].x = self.snake[i - 1].x
			self.snake[i].y = self.snake[i - 1].y
			i-=1

		if self.snake[0].x > self.width:
			self.snake[0].x = 0
		if self.snake[0].x < 0:
			self.snake[0].x = self.width
		if self.snake[0].y > self.height:
			self.snake[0].y = 0
		if self.snake[0].y < 0:
			self.snake[0].y = self.height

		if self._dir == 0:
			self.snake[0].x += self.w
		elif self._dir == 1:
			self.snake[0].x -= self.w
		elif self._dir == 2:
			self.snake[0].y += self.w
		elif _dir == 3:
			self.snake[0].y -= self.w

		for rect in self.snake:
			rect.change()


#Start settiongs 
pygame.init()

SNAKE_WIDTH = 30

WIDTH = SNAKE_WIDTH * 20
HEIGHT = SNAKE_WIDTH * 20

mainLoop = True

bg_color = [0,0,0]

#----------------------------

window = Window(WIDTH,HEIGHT)

window.info()

field = Field(WIDTH,HEIGHT,[0,0,0])
snake = Snake(0,0,SNAKE_WIDTH,SNAKE_WIDTH,WIDTH,HEIGHT)

while mainLoop:
	pygame.time.wait(100)
	for event in pygame.event.get():
		if event.type == QUIT:
			mainLoop = False
		
	window.get_window().fill(bg_color)

	snake.move()
	snake.draw_snake(window.get_window())

	field.draw_field(window.get_window(),SNAKE_WIDTH)

	pygame.display.update()

pygame.quit()


