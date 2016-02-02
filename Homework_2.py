from Tkinter import *
from random import randint
from time import sleep,time
from math import sqrt

#Draw a Canvas for the game
H=600
W= 800
window=Tk()
window.title("Submarine Game")
c=Canvas(window, width= W, height=H, bg="#CAE1FF" )
c.pack()

#Draw a red submarine
ship_c=c.create_oval(300,400,400,430, outline= "red", fill="red")
ship_h=c.create_polygon(370,415,425,400,425,430, outline= "red", fill="red")
ship_p=c.create_rectangle(350,387,360,400, outline= "red", fill="red")
ship_p2=c.create_rectangle(340,387,350,390, outline= "red", fill="red")

#move the submarine

#move up
SHIP_SPD=10
def move_ship_up(event):
	x1,y1,x2,y2 =c.coords(ship_c)
	if y1-SHIP_SPD > 0:
		c.move(ship_c,0,-SHIP_SPD)
		c.move(ship_h,0,-SHIP_SPD)
		c.move(ship_p,0,-SHIP_SPD)
		c.move(ship_p2,0,-SHIP_SPD)
window.bind("<Up>", move_ship_up)

#move down
SHIP_SPD1=-10
def move_ship_down(event):
	x1,y1,x2,y2 =c.coords(ship_c)
	if y2-SHIP_SPD1 < 640:
		c.move(ship_c,0,-SHIP_SPD1)
		c.move(ship_h,0,-SHIP_SPD1)
		c.move(ship_p,0,-SHIP_SPD1)
		c.move(ship_p2,0,-SHIP_SPD1)
window.bind("<Down>", move_ship_down)

#move right
SHIP_SPD2=0
def move_ship_right(event):
	x1,y1,x2,y2 =c.coords(ship_c)
	if x1-SHIP_SPD1 < 730:
		c.move(ship_c,10,-SHIP_SPD2)
		c.move(ship_h,10,-SHIP_SPD2)
		c.move(ship_p,10,-SHIP_SPD2)
		c.move(ship_p2,10,-SHIP_SPD2)
window.bind("<Right>", move_ship_right)

#moveleft
SHIP_SPD3=0
def move_ship_left(event):
	x1,y1,x2,y2 =c.coords(ship_c)
	if x2-SHIP_SPD1 > 80:
		c.move(ship_c,-10,-SHIP_SPD3)
		c.move(ship_h,-10,-SHIP_SPD3)
		c.move(ship_p,-10,-SHIP_SPD3)
		c.move(ship_p2,-10,-SHIP_SPD3)
window.bind("<Left>", move_ship_left)

#Mines:
#	Because Python is object oriented, a single dictionary can be used to keep track of the mines, in place of three separate lists.
#	Mine IDs constitute the key-values of each dictionary entry, while a tuple of (radius, speed) constitute data-values
#	To find a given ID's radius, use "mines[your_mine's_id][0]". To find speed, use "mines[your_mine's_id][1]".

mines = {}

def create_mine():
        radius = randint(0,75)
        x = randint(radius,600-radius)
        y = randint(radius,800-radius)
        speed = randint(5,10)
        mine_id = c.create_oval(x-radius, y+radius, x+radius, y-radius, outline="blue")

        mines[mine_id] = (radius, speed)
        
def mov_mines():
	for mine_id in mines:
		x1,y1,x2,y2 = c.coords(mine_id)
		c.move(mine_id,0,-mines[mine_id][1]) 


#main game loop
NUM_MINES = 3
for x in range(0,NUM_MINES):
	create_mine() 
while time()<END:
	mov_mines()
	if randint(1,50)==1:
		create_mine()
	#clean_up_mines() #you need to create this function
	#collision()#you need to create this function
	window.update()
	sleep(0.1)


