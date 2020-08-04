import pygame

class Window:
    def __init__(self, width=500, height=500):
        self.SCREEN_WIDTH = max(200, width)
        self.SCREEN_HEIGHT = max(200, height)
        self.win = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT], pygame.RESIZABLE)

    def refresh(self, window, box, particles, PGun):
        self.win.fill((255,255,255))
        box.draw(window)
        for p in particles:
            p.draw(window)

        PGun.draw(window)

        pygame.display.update()

    def refresh(self, window, box, particles):
        self.win.fill((255,255,255))
        box.draw(window)
        for p in particles:
            p.draw(window)

        pygame.display.update()
