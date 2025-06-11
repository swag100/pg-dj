import numpy as np

#CONSTANTS
WINDOW_SIZE = (640, 480)
FRAMERATE = 60 #0: unlimited, should be 60

def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def resample(arr, new_length):
    chunkSize = len(arr) // new_length
    return [np.mean(chunk) for chunk in chunks(arr, chunkSize)]