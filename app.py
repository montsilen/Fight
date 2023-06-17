import sys

import lib.control

control = lib.control.control(sys.path[0])

while control.running:
    control.update()

control.quit()