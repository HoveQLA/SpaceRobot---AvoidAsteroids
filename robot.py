#the libraries we gonna use
import math, numpy, pyglet, obstacle, guy, res, random
from copy import copy
from scipy import *



game_window = pyglet.window.Window(900, 750)#setting up the window
white = (255,255,255,255)
pyglet.gl.glClearColor(*white)
main_batch = pyglet.graphics.Batch()

#random coordinates of object (the initial position of the robot and the obstacles)
Num_Asteroid = 10
x_coord = [100]+[random.randint(170, 770) for i in range(Num_Asteroid + 1)]
y_coord = [100]+[random.randint(170, 650) for i in range(Num_Asteroid + 1)]
coord = list(zip(x_coord,y_coord))


goal = [820,720]#fixing the coordinate of the goal

#placing out the object on the window
target = pyglet.sprite.Sprite(img=res.goal,x=goal[0], y=goal[1], batch=main_batch)
obs = [pyglet.sprite.Sprite(img=res.obstacle,x=x_coord[i], y=y_coord[i], batch=main_batch) for i in range(1,len(x_coord)-1)]
objet = pyglet.sprite.Sprite(img=res.player,x=x_coord[0], y=y_coord[0], batch=main_batch)


#function to calculate the distance between two points
def dist(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
 

@game_window.event # function to draw objects on the window
def on_draw():
    game_window.clear()    
    main_batch.draw()



extlen = 10#the extension distance

#function to create the next step point of the robot by following the direction from the robot to the target and the unitary normal direction  
def ef(src, target):
	global extlen
	direction = [goal[i]-src[i] for i in range(len(src))]
	normdir = [direction[i]/dist([0,0], direction) for i in [0,1]]
	return [src[0] + extlen*normdir[0], src[1] + extlen*normdir[1]],normdir

#function to find the nearest obstacle and its separate distance with the robot
def mdit_obs(obs,newpt):
	mdist = min(dist(newpt,[obs1.x,obs1.y]) for obs1 in obs)
	for obs1 in obs :
		if dist(newpt,[obs1.x,obs1.y])==mdist :
			nearobs=[obs1.x,obs1.y]
	return mdist , nearobs


#function to create the next step point of the robot by following the normal direction of the direction from the robot to the target and its unitary normal direction  
def ef1(src, nearobs):
	global extlen
	d=dist(scr,nearobs)
	normdir=[-(scr[1]-nearobs[1])/d,(scr[0]-nearobs[0])/d] 
	return [src[0] + extlen*normdir[0], src[1] + extlen*normdir[1]],normdir


#initializing global variables
scr=coord[0]
d=dist(scr,goal)
normdir=[(scr[0]-goal[0])/d,(scr[1]-goal[1])/d]

#function to update the position of the robot
def update(dt):
	global scr, objet, target, coord , obs , normdir 
	newpt,normdir=ef(scr, target)#new point of the robot by following the direction from the robot to the target 

	mdist,nearobs = mdit_obs(obs,newpt)#nearest obstacle and its separate distance with the robot

	if mdist > 65:#if there is no collision to the new point (mdist > 65) then extend the robot to the new point
		objet.rotation = -270*math.atan2(normdir[0],normdir[1])/math.pi#changing the direction of the robot to the target
		objet.x, objet.y=newpt[0],newpt[1]#moving the robot to the new point
		scr=[objet.x, objet.y]#saving the new position of the robot
	else :#if collision then rotate the robot to the left with 90 degree and extend it 
		newpt,normdir=ef1([objet.x, objet.y], nearobs)#new point of the robot by following the normal direction of the direction from the robot to the target 
		objet.rotation = 100*math.atan2(normdir[0],normdir[1])/math.pi#rotating of 90degree to the left of the robot
		objet.x, objet.y=newpt[0],newpt[1]#moving the robot to the new point
		scr=[objet.x, objet.y]#saving the new position of the robot
	if dist(scr, goal)<=20:
		return
       


if __name__ == "__main__":
    # Update the game 5 times per second
    pyglet.clock.schedule_interval(update, 1/5.0)        
    # Tell pyglet to do its thing
    pyglet.app.run()

