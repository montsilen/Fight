import lib.control

control = lib.control.control()

while control.running:
    control.update()

control.quit()