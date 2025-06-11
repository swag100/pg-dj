import pygame
import utils
import waveform

class Game:
    def __init__(self):
        pygame.init()

        width, height = utils.WINDOW_SIZE
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        self.done = False

        self.wav = waveform.Waveform("FL stock.wav", pygame.Rect(0, 0, width, height))
        self.float_x = self.wav.rect.x

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            else:
                pass #state handles event

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.float_x += utils.WINDOW_SIZE[0] / self.wav.duration * dt #use sample length for 1 second? i think?
        if keys[pygame.K_d]:
            self.float_x -= utils.WINDOW_SIZE[0] / self.wav.duration * dt
        
        self.wav.rect.x = self.float_x

    def draw(self):
        self.screen.fill((0,0,0))

        self.wav.draw(self.screen)

        font = pygame.font.SysFont("Arial", 18) 
        fps = str(int(self.clock.get_fps()))
        fps_text = font.render(fps, 1, pygame.Color("coral"))
        self.screen.blit(fps_text, (10, 0))

    def start(self):
        while not self.done:
            dt = self.clock.tick(utils.FRAMERATE) / 1000

            self.handle_events()
            self.update(dt)
            self.draw()

            pygame.display.flip()

        pygame.quit()

Game().start()