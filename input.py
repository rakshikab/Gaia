from OpenGL.GLUT import *
from utils import Vector
from math import sin, cos

class Input:
    
    xOrigin = 0
    yOrigin = 0
    polarangle = 0.0
    azimuthalangle = 0.0
    deltaMove = 0
    deltaTilt = 0
    deltaVertical = 0
    deltapolarangle = 0
    deltaazimuthalangle = 0
    deltafov = 0
    strafe = 0
    panvector = Vector(0.0, 0.0, 0.0)


    def pressNormalKey(self, key, xx, yy):
        if key == 27:
            exit(0)
        if key == 'w' or key == 'W':
            self.deltaVertical = 1
        if key == 's' or key == 'S':
            self.deltaVertical = -1
        if key == 'm' or key == 'M':
            self.deltaTilt = -1
        if key == 'n' or key == 'N':
            self.deltaTilt = 1

    def releaseNormalKey(self, key, xx, yy):
        if key == 'w' or key == 'W' or key == 's' or key == 'S':
            self.deltaVertical = 0
        if key == 'm' or key == 'M' or key == 'n' or key == 'N':
            self.deltaTilt = 0

    # Forward and backward movement, strafing keys
    def pressKey(self, key, xx, yy):
        if key == GLUT_KEY_UP:
            self.deltaMove=1
        elif key == GLUT_KEY_DOWN:
            self.deltaMove=-1
        elif GLUT_KEY_RIGHT:
            self.strafe=-1
        elif GLUT_KEY_LEFT:
            self.strafe=1


    def releaseKey(self, key, x, y):

        if key == GLUT_KEY_UP or key == GLUT_KEY_DOWN:
            self.deltaMove = 0
        if key == GLUT_KEY_LEFT or key == GLUT_KEY_RIGHT:
            self.strafe = 0

    def mouseButton(self, button, state, x, y):
        if(button == GLUT_LEFT_BUTTON):
            if(state == GLUT_UP):
                self.polarangle += self.deltapolarangle
                self.xOrigin = -1
                self.azimuthalangle += self.deltaazimuthalangle
                self.yOrigin = -1
            else:
                self.xOrigin = x
                self.yOrigin = y

        if (button == 3 or button == 4):
            if (state == GLUT_DOWN):
                pass#Camera.zoom(-0.5) if button == 3 else Camera.zoom(0.5)

    def mouseMove(self, x, y):
        if(self.xOrigin >= 0):
            self.deltapolarangle = (self.xOrigin - x) * 0.003

            self.panvector.x = cos(self.polarangle + self.deltapolarangle)
            self.panvector.z = -sin(self.polarangle + self.deltapolarangle)
    
        if(self.yOrigin >= 0):
            self.deltaazimuthalangle = (self.yOrigin - y) * 0.003
            self.panvector.y = sin(self.azimuthalangle + self.deltaazimuthalangle)
    
