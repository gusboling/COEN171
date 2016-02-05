from Tkinter import *
from random import randint
from time import sleep,time
from math import *

#Draw a Canvas for the game
SCORE = 0
H = 600
W = 800
window = Tk()
window.title("Submarine Game")
c = Canvas(window, width= W, height=H, bg="#CAE1FF" )
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
#	To find a given ID's radius, use "mines[your_mine's_id][0]". To find speed, use "mines[your_mine's_id][1]", etc.

mines = {}

def create_mine():
        radius = randint(25,75)
        x = randint(radius,600-radius)
        y = randint(radius,800-radius)
        speed = randint(1,5)
        mine_id = c.create_oval(x-radius, y+radius, x+radius, y-radius, outline="blue")

        mines[mine_id] = (radius, speed, x, y)
        
def mov_mines():
	if len(mines) != 0:
		for mine_id in mines:
			#x1,y1,x2,y2 = c.coords(mine_id) #commmented out - serves no discernable purpose.
			c.move(mine_id,0,-mines[mine_id][1]) 

def clean_up_mines():
	garbage_ids = []
	for mine_id in mines:
		if (c.coords(mine_id)[1]) <= -200:
			garbage_ids.append(mine_id)
	for gid in garbage_ids:
		c.delete(gid)
		try:
			del mines[gid]
			#print("Mine_ID %d Deleted Succefully. \n" % gid)
		except:
			print("Problem Deleting Mine_ID %d. \n" % gid)
	return


def distance(pointA, pointB):
	deltaX2 = pow(pointB[0] - pointA[0], 2)
	deltaY2 = pow(pointB[1] - pointA[1], 2)
	distVal = sqrt(deltaY2+deltaX2)
	return distVal

def collision():
	garbage_ids = []
	current_score = SCORE

	ship_coord = c.coords(ship_h)
	ship_top = [ship_coord[0], ship_coord[3]]
	ship_bot = [ship_coord[0], ship_coord[5]]
	ship_lef = [ship_coord[0]-100, ship_coord[1]]
	ship_rig = [ship_coord[0]+100, ship_coord[1]]
	points = [ship_top, ship_bot, ship_lef, ship_rig]

	for mine in mines:
		mine_coord = c.coords(mine)
		mine_x_cent = mine_coord[0]+((mine_coord[2]-mine_coord[0])/2)
		mine_y_cent = mine_coord[1]+((mine_coord[3]-mine_coord[1])/2)
		mine_cent = [mine_x_cent, mine_y_cent]
	
		for point in points:
			if distance(point, mine_cent) < mines[mine][0]:
				#print("Collision Detected! \n")
				current_score += 1
				garbage_ids.append(mine)

	for gid in garbage_ids:
		try:
			c.delete(gid)
			del mines[gid]
		except:
			print("Collision Error Mine_ID %d. \n" % gid)

	return current_score


#main game loop
NUM_MINES = 5
END = time()+60
c.create_text(150,30, text='SCORE', fill='black')
score_text = c.create_text(150, 50, fill='black')
c.create_text(100, 30, text='TIME', fill='black')
time_text = c.create_text(100, 50, fill='black')

def show_time(time_rem):
	c.itemconfig(time_text, text=str(time_rem))

def show_score(score):
	c.itemconfig(score_text, text=str(score))

for x in range(0,NUM_MINES):
	create_mine()

while time()<END:
	mov_mines()
	if randint(1,50)==1:
		create_mine()
	clean_up_mines()
	SCORE = collision()
	show_score(SCORE)
	show_time(int(END - time()))
	window.update()
	sleep(0.05)























"""This code was created on January 1, 2016 by Augustus Boling."""