from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from copy import deepcopy

euler = [45.0, 45.0, 45.0]
last_euler = [0, 0, 0]
acc = [10, 0, 0]

def draw():
    global last_euler
    glClear(GL_COLOR_BUFFER_BIT)

    glRotatef(euler[0] - last_euler[0], 1, 0, 0)
    glRotatef(euler[1] - last_euler[1], 0, 1, 0)
    glRotatef(euler[2] - last_euler[2], 0, 0, 1)
    last_euler = deepcopy(euler)
    glutWireCube(0.7)
    glFlush()


def loop(value):
    euler[0] += 1
    glutPostRedisplay()
    glutTimerFunc(16, loop, 0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow('Test')
    glutDisplayFunc(draw)
    glutTimerFunc(16, loop, 0)
    glutMainLoop()


if __name__ == '__main__':
    main()
