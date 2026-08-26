import obj,res

class Obstacle(obj.Obj):
    """An asteroid that divides a little before it dies"""
    
    def __init__(self, *args, **kwargs):
        super(Obstacle, self).__init__(img=res.obstacle, *args, **kwargs)        
                
       
