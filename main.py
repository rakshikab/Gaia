from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

from objreader import OBJreader
from object import Object
from primitives import Plane, RandomizedHeightMapGrid

name = 'Environment'
scene = []

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
    glutMainLoop()
    return

def display():
    glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)
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
