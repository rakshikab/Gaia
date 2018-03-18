class Primitive(object):
    def __init__(self):
        self.vertices = []
        self.faces = []
        self.bbox = []

class Grid(Primitive):
    def __init__(self, width, length):
        super(Grid, self).__init__()
        self.vertices.append((-width/2, 0, -length/2))
        self.vertices.append((-width/2, 0, length/2))
        self.vertices.append((width/2, 0, length/2))
        self.vertices.append((width/2, 0, -length/2))
        
        self.faces.append((0, 1, 2))
        self.faces.append((2, 3, 0))        
        self.bbox = ((-width/2, -length/2),(0,0),(width/2, length/2))
        
        
