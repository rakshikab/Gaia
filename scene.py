from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from input import *
from camera import Camera

class Scene:
    name = 'Environment'
    fov = 45.0
    width = 400
    height = 400

    def main(self):
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(self.width, self.height)
        glutCreateWindow(self.name)
        glutReshapeFunc(self.windowResize)

        glClearColor(0.,0.,0.,1.)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        lightZeroPosition = [10.,4.,10.,1.]
        lightZeroColor = [0.8,1.0,0.8,1.0] #green tinged
        glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHT0)
        glutDisplayFunc(self.display)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(40.,1.,1.,40.)
        glMatrixMode(GL_MODELVIEW)
        gluLookAt(0,0,10,
                  0,0,0,
                  0,1,0)
        glPushMatrix()

        # Keyboard event processing
        glutIgnoreKeyRepeat(1)
        input = Input()
        glutKeyboardFunc(input.pressNormalKey)
        glutKeyboardUpFunc(input.releaseNormalKey)
        glutSpecialFunc(input.pressKey)
        glutSpecialUpFunc(input.releaseKey)

        # Mouse event processing
        glutMouseFunc(input.mouseButton)
        glutMotionFunc(input.mouseMove)

        glutMainLoop()
        return

    def windowResize(self, w, h):
        # Set up perspective projection
        aspratio =  w * 1.0 / h
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glViewport(0, 0, w, h)
        gluPerspective(self.fov, aspratio, 0.1, 1000.0)
        glMatrixMode(GL_MODELVIEW)

        # Update scene settings for width and height
        self.width = w
        self.height = h

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        color = [1.0,0.,0.,1.]
        glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
        glutSolidSphere(2,20,20)
        glPopMatrix()
        camera = Camera()
        camera.update()
        camera.solve()
        glutSwapBuffers()
        return
