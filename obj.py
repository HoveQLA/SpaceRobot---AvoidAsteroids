import pyglet
import res

class Obj(pyglet.sprite.Sprite):
    """A sprite with physical properties such as velocity"""
    
    def __init__(self, *args, **kwargs):
        super(Obj, self).__init__(*args, **kwargs)
    
    def update(self, dt):
        """This method should be called every frame."""
                       
        # Wrap around the screen if necessary
        self.check_bounds()
    
    def check_bounds(self):
        """Use the classic Asteroids screen wrapping behavior"""
        min_x = -self.image.width/2
        min_y = -self.image.height/2
        max_x = resources.MAX_X + self.image.width/2
        max_y = resources.MAX_Y + self.image.height/2
        if self.x < min_x:
            self.x = max_x
        if self.y < min_y:
            self.y = max_y
        if self.x > max_x:
            self.x = min_x
        if self.y > max_y:
            self.y = min_y
    

