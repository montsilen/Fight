import pygame.mixer

class backgroundMusicMixer:
    def __init__(self, dir) -> None:
        pygame.mixer.music.load(dir + "/assets/music/BackgroundMusic.mp3")
        self.basedir = dir
        self.backgroundMusicOn = True
        self.backgroundMusicVolume = 80
        pygame.mixer.music.set_volume(self.backgroundMusicVolume / 100)
        pygame.mixer.music.play()

    def changeBackgroundMusicStatus(self):
        self.backgroundMusicOn = not self.backgroundMusicOn
        if self.backgroundMusicOn:
            pygame.mixer.music.rewind()
        else:
            pygame.mixer.music.fadeout()

    def setBackgroundMusicStatus(self, volume):
        self.backgroundMusicVolume = volume
        pygame.mixer.music.set_volume(self.backgroundMusicVolume / 100)

