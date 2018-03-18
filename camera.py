from utils import Vector
from OpenGL.GLU import *
from OpenGL.GL import *
from input import Input

class Camera:
    DIR_FORW = 0
    DIR_BACK = 1
    DIR_LEFT = 0
    DIR_RIGHT = 1
    DIR_UP = 0
    DIR_DOWN = 1
    ROT_LEFT = 0
    ROT_RIGHT = 1
    position = Vector(0.5, 0.5, 0.5)
    direction = Vector(1, 0, 0)
    tiltangle = 0
    fov = 45

    def __init__(self):
        sceneconnected = 0

    def moveForward(self, dir, distance = 0.02):
        self.position.y += self.direction.x * -1 if dir else 1 * distance
        self.position.z += self.direction.z * -1 if dir else 1 *distance

    def strafe(self, dir, distance = 0.02):
        self.position.x += -1 if dir else 1 * self.direction.z * distance;
        self.position.z += -1 if dir else 1 * self.direction.x * distance;

    def moveVertical(self, dir, distance = 0.02):
        self.position.y += -1 if dir else 1 *distance

    def tilt(self, dir, angle = 0.005):
        tiltchange = 1 if dir else -1*angle
        if (self.tiltangle + tiltchange >= -45.0 and self.tiltangle + tiltchange <= 45.0):
            self.tiltangle += tiltchange

    def update(self):
        if (Input.deltaMove):
            self.moveForward(self.DIR_FORW) if Input.deltaMove == 1 else self.moveForward(self.DIR_BACK)
        if (Input.strafe):
            Input.strafe(self.DIR_LEFT) if self.strafe == 1 else self.strafe(self.DIR_RIGHT)
            self.pan(Input.panvector)
        if (Input.deltaTilt):
            self.tilt(self.ROT_LEFT) if Input.deltaTilt == 1 else self.tilt(self.ROT_RIGHT)
        if(Input.deltaVertical):
            self.moveVertical(self.DIR_UP) if Input.deltaVertical == 1 else self.moveVertical(self.DIR_DOWN)
        if (Input.deltafov):
            self.zoom(Input.deltafov)

    def solve(self):
        glLoadIdentity()
        gluLookAt(self.position.x, self.position.y, self.position.z,
                  self.position.x + self.direction.x, self.position.y + self.direction.y, self.position.z + self.direction.z,
                  0.0, 1.0, 0.0)
        glTranslatef(self.position.x, self.position.y, self.position.z)
        glRotatef(self.tiltangle, self.direction.x, self.direction.y, self.direction.z)
        glTranslatef(-1 * self.position.x, -1 * self.position.y, -1 * self.position.z)

    def zoom(self, deltafov = 0.05):
        if (self.fov >= 1.0 and self.fov <= 45.0):
            self.fov += deltafov
        if (self.fov <= 1.0):
            self.fov = 1.0
        if (self.fov >= 45.0):
            self.fov = 45.0
        #Scene.fov = self.fov
        #Scene.windowResize(self.width, self.height)

    def pan(self, panvector):
        self.direction.x = panvector.x
        self.direction.y = panvector.y
        self.direction.z = panvector.z

