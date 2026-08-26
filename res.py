import pyglet

def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width//2
    image.anchor_y = image.height//2

obstacle = pyglet.image.load("asteroid.png")
center_image(obstacle)

player = pyglet.image.load("player.png")
center_image(player)

goal = pyglet.image.load('goal.png')
center_image(goal)


