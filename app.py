import sys

from lib import control

control = control.control(sys.path[0])

while control.running:
    control.update()

control.quit()