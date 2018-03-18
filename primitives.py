import random

class Primitive(object):
    def __init__(self):
        self.vertices = []
        self.faces = []
        self.bbox = []

class Plane(Primitive):
    def __init__(self, width, length):
        super(Plane, self).__init__()
        self.vertices.append((-width/2.0, 0, -length/2.0))
        self.vertices.append((-width/2.0, 0, length/2.0))
        self.vertices.append((width/2.0, 0, length/2.0))
        self.vertices.append((width/2.0, 0, -length/2.0))
        
        self.faces.append((0, 1, 2))
        self.faces.append((2, 3, 0))        
        self.bbox = ((-width/2.0, -length/2.0),(0,0),(width/2.0, length/2.0))
       
class Grid(Primitive):
    def __init__(self, width, length, divisions=0):
        super(Grid, self).__init__()
        spacing_x = width*1.0/(2+divisions)
        spacing_y = length*1.0/(2+divisions)
        n_x = 2+divisions
        n_y = 2+divisions
        
        # Draw vertices
        for i in xrange(n_x):
            for j in xrange(n_y):
                x = -width/2.0 + i*spacing_x
                y = -length/2.0 + j*spacing_y
                self.vertices.append([x, 0, y])
        
        # Connect vertices for faces
        for i in xrange(n_x-1):
            for j in xrange(n_y-1):
                vertex_id = j*n_x + i
                self.faces.append((vertex_id, vertex_id+1, vertex_id+1+n_x))
                self.faces.append((vertex_id+1+n_x, vertex_id+n_x, vertex_id))             
                
class RandomizedHeightMapGrid(Grid):
    def __init__(self, width, length, divisions=0, amplitude=1):
        super(RandomizedHeightMapGrid, self).__init__(width, length, divisions)
        rows = columns = 2+divisions
        randomized_heightmap = [[random.random()*amplitude for x in range(columns)] for x in range(rows)]
        
        for i in xrange(rows):
            for j in xrange(columns):
                vertex_id = j*rows + i
                vertex = self.vertices[vertex_id]
                vertex[1] = randomized_heightmap[i][j]
