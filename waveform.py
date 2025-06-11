import pygame
import numpy
import utils
from scipy.io import wavfile

class Waveform:
    def __init__(self, filename, rect):
        #Read file and get sampling freq [ usually 44100 Hz ]  and sound object
        self.rate, self.data = wavfile.read('sounds/' + filename)


        self.data = self.data / (2**15)

        self.rect = rect

        # We can represent sound by plotting the pressure values against time axis.
        #Create an array of sample point in one dimension
        #self.time_array = (numpy.arange(0, float(self.data.shape[0]), 1) / self.rate) * 1000
        self.time_array = numpy.arange(0, float(self.data.shape[0]), 1) / self.rate

        #Get duration of sound file
        self.duration = self.time_array[-1]

        self.image = self.get_image()

    def get_image(self, channel = 0):
        new_surface = pygame.Surface((self.rect.w, self.rect.h), pygame.SRCALPHA)

        #gets worse the longer the sound becomes.
        x_data = utils.resample(self.time_array, int(self.rect.w * self.duration)) 
        y_data = utils.resample(self.data[:,channel], int(self.rect.w * self.duration))
        
        # Draw the line graph
        for i in range(len(x_data) - 1):
            x1 = x_data[i] * (self.rect.w / self.duration)
            y1 = y_data[i] * (self.rect.h / 2) + (self.rect.h / 2)

            x2 = x_data[i + 1] * (self.rect.w / self.duration)
            y2 = y_data[i + 1] * (self.rect.h / 2) + (self.rect.h / 2)

            pygame.draw.line(new_surface, (0, 0, 255), (x1, y1), (x2, y2), 1)

        return new_surface

    def draw(self, screen):
        screen.blit(self.image, self.rect)