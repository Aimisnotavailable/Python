import pygame
import sys
from brains import Brains
from buttons import Button



class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((600, 400))
        self.display = pygame.Surface((300, 200))
        self.brain = Brains()
        self.guesses = self.brain.load()
        self.buttons = []
        pygame.init()
        self.f_size = 15
        self.font = pygame.font.Font(size=self.f_size)
        text = "Start"
        self.start = Button((150, 100), (25, 15), (0, 255, 0), text=text)
        self.buttons.append(self.start)
        self.clock = pygame.time.Clock()

        print(self.guesses)


    def run(self):

        while True:

            self.display.fill((100, 100, 100))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.brain.save()
                    pygame.quit()
                    sys.exit()
                

            for button in self.buttons:
                if button.show:
                    button.render(self.display, self.font)

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()))
            pygame.display.update()
            self.clock.tick(60)


Game().run()