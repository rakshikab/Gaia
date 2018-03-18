class OBJreader:
    def __init__(self, filename):
        self.vertices = []
        self.bbox = []
        self.faces = []
        self.filename = filename
        self.parseOBJ()
        self.bbox = self.calculateBoundingBox()
        
    def parseOBJ(self):
        file = open(self.filename,"r")
        for line in file:
            if line[0]=='v' and line[1]==' ':
                comps = line.strip().split(' ')
                self.vertices.append([float(comps[1]),float(comps[2]),float(comps[3])])
            elif line[0]=='f':
                comps = line.strip().split(' ')
                vertinds = [int(faceatt.split('/')[0]) for faceatt in comps[1:]]
                l = len(vertinds)
                for i in xrange(l-2):
                    self.faces.append([vertinds[i+1]-1,vertinds[i+2]-1,vertinds[0]-1])
        file.close()
        
    def calculateBoundingBox(self):
        xs = [t[0] for t in self.vertices]
        ys = [t[1] for t in self.vertices]
        zs = [t[2] for t in self.vertices]
        return ((min(xs), max(xs)), (min(ys), max(ys)), (min(zs), max(zs)))
        
