import obj, res

# General Spaceship object. This class handles all the graphics and general behaviour of the spaceship class

class Guy(obj.Obj):
    """General Spaceship Object"""
    
    def __init__(self, *args, **kwargs):
        super(Guy, self).__init__(img=res.player, *args, **kwargs)
    
