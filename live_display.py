import sys
from copy import deepcopy

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import pandas as pd

euler = [0, 0, 0]
last_euler = [0, 0, 0]
acc = [10, 0, 0]
last_length_read = 0

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
    global last_length_read
    data = pd.read_csv(sys.argv[1])
    pandas_euler = data.iloc[len(data) - 1][1:4]
    euler[0] = -pandas_euler.iloc[2]
    euler[1] = pandas_euler.iloc[0]
    euler[2] = -pandas_euler.iloc[1]
    glutPostRedisplay()
    glutTimerFunc(16, loop, 0)

def main():
    assert len(sys.argv) == 2, f'1 parameter, file name and interval, needed ({len(sys.argv) - 1} parameters given)'
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutCreateWindow('Test')
    glutDisplayFunc(draw)
    glutTimerFunc(16, loop, 0)
    glutMainLoop()


if __name__ == '__main__':
    main()
