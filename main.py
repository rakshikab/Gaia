from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
from math import sin, cos

from objreader import OBJreader
from object import Object
from primitives import Plane, RandomizedHeightMapGrid

name = 'Environment'
scene = []
XZangle = 0.0
Yangle = 0.0
axisangle = 0.0

cameraX = 0.0
cameraZ = 5.0
cameraY = 1.0

vx =  0.0
vz = -1.0
vy =  0.0

deltaXZangle = 0.0
deltaYangle = 0.0

deltaMove = 0
xOrigin = -1
yOrigin = -1
lstrafe = 0
rstrafe = 0

rollamount = 0
fov = 45.0

def changeSize(w, h):
    ratio = w * 1.0 / h

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glViewport(0, 0, w, h)
    gluPerspective(fov, ratio, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def loadMeshes():
    tree_mesh = OBJreader('models/tree.obj')
    #plane_mesh = Plane(30, 30)
    plane_mesh = RandomizedHeightMapGrid(30, 30, 150, 0.2)

    tree1 = Object('tree1', tree_mesh)
    tree2 = Object('tree2', tree_mesh)
    tree3 = Object('tree3', tree_mesh)
    ground_plane = Object('plane1', plane_mesh)

    tree1.translate(-2, -2, 1)
    tree2.translate(0, -2, 0)
    tree3.translate(2, -2, -5)
    ground_plane.translate(5, -1, 0)

    tree1.setColor(0.2, 1.0, 0.2, 1.0)
    tree2.setColor(0.5, 1.0, 0.4, 1.0)
    tree3.setColor(0.3, 1.0, 0.3, 1.0)
    ground_plane.setColor(1.0, 1.0, 1.0, 1.0)

    scene.append(tree1)
    scene.append(tree2)
    scene.append(tree3)
    scene.append(ground_plane)

def computePos(deltaMove):
    global cameraX, cameraY, cameraZ, vx, vy, vz
    if (lstrafe):
        cameraX += vz * 0.5
        cameraZ += (-vx) * 0.5

    elif (rstrafe):
        cameraX += (-vz) * 0.5
        cameraZ += vx * 0.5

    else:
        cameraX += deltaMove * vx * 0.5
        cameraZ += deltaMove * vz * 0.5

def processNormalKeys(key, xx, yy):
    global rollamount, cameraY
    key = str(key)
    if (key == 27):
        exit(0)
    if (key == 'W' or key == 'w'):
        cameraY += 0.5
    if (key == 'S' or key == 's'):
        cameraY -= 0.5
    if (key == 'M' or key == 'm'):
        if (rollamount > -45):
            rollamount -= 1
    if (key == 'N' or key == 'n'):
        if (rollamount < 45):
            rollamount += 1

def pressKey(key, xx, yy):
    global deltaMove, lstrafe, rstrafe

    if key == GLUT_KEY_UP:
        deltaMove = 0.8
    elif key == GLUT_KEY_DOWN:
        deltaMove = -0.8
    elif key == GLUT_KEY_RIGHT:
        rstrafe = 1
    elif key == GLUT_KEY_LEFT:
        lstrafe = 1

def releaseKey(key, x, y):
    global deltaMove, lstrafe, rstrafe

    if key == GLUT_KEY_UP or key == GLUT_KEY_DOWN:
        deltaMove = 0
    elif key == GLUT_KEY_LEFT:
        lstrafe = 0
    elif key == GLUT_KEY_RIGHT:
        rstrafe = 0

def mouseMove(x, y):
    global vx, vy, vz, deltaXZangle, xOrigin, XZangle, yOrigin, deltaYangle, Yangle

    if(xOrigin >= 0):
        deltaXZangle = (x - xOrigin) * 0.010

        vx = sin(XZangle + deltaXZangle)
        vz = -cos(XZangle + deltaXZangle)

    if(yOrigin >= 0):
        deltaYangle = (yOrigin - y) * 0.006
        vy = sin(Yangle + deltaYangle)

def mouseButton(button, state, x, y):
    global fov, XZangle, Yangle, xOrigin, yOrigin, deltaXZangle, deltaYangle

    if(button == GLUT_LEFT_BUTTON):
        if(state == GLUT_UP):
            XZangle += deltaXZangle
            xOrigin = -1
            Yangle += deltaYangle
            yOrigin = -1
        else:
            xOrigin = x
            yOrigin = y


    if (button == 3 or button == 4):
        if(fov >= 1.0 and fov <= 45.0):
            fov += -1 if button == 3 else 1
        if(fov <= 1.0):
            fov = 1.0
        if(fov >= 45.0):
            fov = 45.0

        w = glutGet(GLUT_WINDOW_WIDTH)
        h = glutGet(GLUT_WINDOW_HEIGHT)

        ratio =  w * 1.0 / h
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glViewport(0, 0, w, h)
        gluPerspective(fov, ratio, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400,400)
    glutCreateWindow(name)

    glClearColor(135/255.0, 206/255.0, 250/255.0, 1.0)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    lightZeroPosition = [10.0, 4.0, 10.0, 1.0]
    lightZeroColor = [0.8, 0.8, 0.2, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    glutDisplayFunc(display)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40.0, 1.0, 1.0, 40.0)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0,0,10,
              0,0,0,
              0,1,0)
    loadMeshes()
    glPushMatrix()
    glutReshapeFunc(changeSize)

    glutIgnoreKeyRepeat(1)
    glutKeyboardFunc(processNormalKeys)
    glutSpecialFunc(pressKey)
    glutSpecialUpFunc(releaseKey)

    glutMouseFunc(mouseButton)
    glutMotionFunc(mouseMove)
    glutIdleFunc(display)
    glutMainLoop()
    return

def display():
    global vx, vy, vz, deltaMove, lstrafe, rstrafe, cameraX, cameraY, cameraZ

    if (deltaMove or lstrafe or rstrafe):
        computePos(deltaMove)

    glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    gluLookAt(cameraX, cameraY, cameraZ,
              cameraX+vx, cameraY+vy, cameraZ+ vz,
              0.0, 1.0,  0.0)
    glTranslatef(cameraX, cameraY, cameraZ)
    glRotatef(rollamount, vx, vy, vz)
    glTranslatef(-1.0 * cameraX, -1.0 * cameraY, -1.0 * cameraZ)

    glPushMatrix()
    # Object rendering code
    for object in scene:
        # Work in this object's space
        glPushMatrix()

        # Apply all object transforms
        glScalef(object.scaling[0], object.scaling[1], object.scaling[2])
        glRotatef(object.rotation[0], 1, 0, 0)
        glRotatef(object.rotation[1], 0, 1, 0)
        glRotatef(object.rotation[2], 0, 0, 1)
        glTranslatef(object.translation[0], object.translation[1], object.translation[2])

        # Set color and material for this object
        color = [object.color[0], object.color[1], object.color[2], object.color[3]]
        glMaterialfv(GL_FRONT, GL_DIFFUSE, color)

        # Draw triangles from the mesh description
        glBegin(GL_TRIANGLES)
        for face in object.mesh.faces:
            for index in face:
                v = object.mesh.vertices[index]
                glVertex3f(v[0], v[1], v[2])
        glEnd()
        # Come back to world space
        glPopMatrix()

    glPopMatrix()
    glutSwapBuffers()
    return

if __name__ == '__main__': main()
