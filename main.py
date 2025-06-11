import pygame
import utils
import scrubber

class Game:
    def __init__(self):
        pygame.init()

        self.width, self.height = utils.WINDOW_SIZE
        self.screen = pygame.display.set_mode(utils.WINDOW_SIZE)
        self.clock = pygame.time.Clock()

        self.done = False

        self.scrubber = scrubber.Scrubber()

        self.float_x = self.scrubber.wav.rect.x

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            else:
                pass #state handles event

    def update(self, dt):
        self.scrubber.update(dt)

    def draw(self):
        self.screen.fill((0,0,0))

        self.scrubber.draw(self.screen)

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