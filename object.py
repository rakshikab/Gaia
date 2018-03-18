class Object:
    def __init__(self, name, mesh):
        self.name = name
        self.mesh = mesh
        self.translation = [0, 0, 0]
        self.rotation = [0, 0, 0]
        self.scaling = [1, 1, 1]
        self.color = [1.0, 1.0, 1.0, 1.0]
        self.bbox = mesh.bbox

    def translate(self, tx, ty, tz, absolute=False):
        if absolute:
            self.translation = [0, 0, 0]
        self.translation[0] += tx
        self.translation[1] += ty
        self.translation[2] += tz

    def rotate(self, rx, ry, rz, absolute=False):
        if absolute:
            self.rotation = [0, 0, 0]
        self.rotation[0] += rx
        self.rotation[1] += ry
        self.rotation[2] += rz
        
    def scale(self, sx, sy, sz, absolute=False):
        if absolute:
            self.scaling = [1, 1, 1]
        self.scaling[0] += sx
        self.scaling[1] += sy
        self.scaling[2] += sz
        
    def setColor(self, r, g, b, a):
        self.color[0] = r
        self.color[1] = g
        self.color[2] = b
        self.color[3] = a
