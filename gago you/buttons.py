import pygame

class Button:

    def __init__(self, pos, size, color, text=''):
        self.surf = pygame.Surface(size)
        self.pos = list(pos)
        self.size = list(size)
        self.color = color
        self.text = text

        self.show = True

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def render(self, surf, font):
        self.surf.fill((0, 0, 0))
        pygame.draw.rect(self.surf, self.color, (0,0, *self.size))
        self.surf.blit(font.render(self.text, False, (100, 100, 100)), (0, 0))
        s_rect = self.surf.get_rect(center=self.pos)
        surf.blit(self.surf, s_rect)