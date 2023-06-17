import pygame, sys

import lib.music.bgmusic

class control:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.tickClock = pygame.time.Clock()
        self.bgmusic = lib.music.bgmusic.backgroundMusicMixer()
        self.running = True

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        pygame.display.update()
        self.tickClock.tick(60)

    def quit(self):
        pygame.quit()
        sys.exit()
