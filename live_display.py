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

def draw_colored_cube(size):
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Front face (colored)
    glColor4f(1.0, 0.0, 0.0, 1.0)  # Red, fully opaque
    glBegin(GL_QUADS)
    glVertex3f(-size, -size, size)
    glVertex3f(size, -size, size)
    glVertex3f(size, size, size)
    glVertex3f(-size, size, size)
    glEnd()

    glColor4f(100.0, 100.0, 100.0, 0.1)
    glBegin(GL_QUADS)
    glVertex3f(-size, -size, -size)
    glVertex3f(size, -size, -size)
    glVertex3f(size, size, -size)
    glVertex3f(-size, size, -size)
    glEnd()

    # Left face (transparent)
    glColor4f(100.0, 100.0, 100.0, 0.1)
    glBegin(GL_QUADS)
    glVertex3f(-size, -size, -size)
    glVertex3f(-size, -size, size)
    glVertex3f(-size, size, size)
    glVertex3f(-size, size, -size)
    glEnd()

    # Right face (transparent)
    glColor4f(100.0, 100.0, 100.0, 0.1)
    glBegin(GL_QUADS)
    glVertex3f(size, -size, -size)
    glVertex3f(size, -size, size)
    glVertex3f(size, size, size)
    glVertex3f(size, size, -size)
    glEnd()

    # Top face (transparent)
    glColor4f(100.0, 100.0, 100.0, 0.1)
    glBegin(GL_QUADS)
    glVertex3f(-size, size, -size)
    glVertex3f(size, size, -size)
    glVertex3f(size, size, size)
    glVertex3f(-size, size, size)
    glEnd()

    # Bottom face (transparent)
    glColor4f(100.0, 100.0, 100.0, 0.1)
    glBegin(GL_QUADS)
    glVertex3f(-size, -size, -size)
    glVertex3f(size, -size, -size)
    glVertex3f(size, -size, size)
    glVertex3f(-size, -size, size)
    glEnd()

    glDisable(GL_BLEND)

def draw():
    global last_euler
    glClear(GL_COLOR_BUFFER_BIT)

    glRotatef(euler[0] - last_euler[0], 1, 0, 0)
    glRotatef(euler[1] - last_euler[1], 0, 1, 0)
    glRotatef(euler[2] - last_euler[2], 0, 0, 1)
    last_euler = deepcopy(euler)
    draw_colored_cube(0.5)
    # glutWireCube(0.7)
    glFlush()


def loop(value):
    global last_length_read
    data = pd.read_csv(sys.argv[1])
    pandas_euler = data.iloc[len(data) - 1][1:4]
    euler[0] = pandas_euler.iloc[1]
    euler[1] = -pandas_euler.iloc[2]
    euler[2] = pandas_euler.iloc[0]
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
