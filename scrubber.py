import pygame
import utils
import waveform

width, height = utils.WINDOW_SIZE

class Scrubber:
    def __init__(self):
        self.wav = waveform.Waveform("pop.wav", pygame.Rect(0, 0, width, 48))

        self.duration = self.wav.duration

        self.position = 0

    def update(self, dt):
        self.position += dt

    def draw(self, screen):
        self.wav.draw(screen)
        pygame.draw.rect(
            screen, 
            (255, 0, 0),
            pygame.Rect(((self.position - 1) % self.duration * (self.wav.rect.w / self.duration)), self.wav.rect.y, 2, self.wav.rect.h)
        )