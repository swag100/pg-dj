import numpy
import pygame
import pyaudio
import waveform

from scipy.io.wavfile import write

class Scrubber:
    def __init__(self):
        self.wav = waveform.Waveform("pop.wav", pygame.Rect(0, 0, 300, 48))

        self.duration = self.wav.duration

        self.position = 0

    def update(self, dt):
        self.position += dt
        
        #scaled = numpy.int16(self.wav.data / numpy.max(numpy.abs(self.wav.data)) * (2**15))
        #write('test.wav', self.wav.rate, scaled)

    def draw(self, screen):
        self.wav.draw(screen)
        pygame.draw.rect(
            screen, 
            (255, 0, 0),
            pygame.Rect(((self.position - 1) % self.duration * (self.wav.rect.w / self.duration)), self.wav.rect.y, 2, self.wav.rect.h)
        )