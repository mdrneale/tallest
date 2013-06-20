import pygame, sys, time
from pygame.locals import *

class Window(object):
    def __init__(self, x, y, name = "", fullscreen = False):
        self.lastFrameTime = self.currentFrameTime = time.clock()
        extra = 0
        if fullscreen:
            extra |= pygame.FULLSCREEN
        pygame.init()
        pygame.display.set_caption(name)
        self.fpsClock   = pygame.time.Clock()
        self.surface    = pygame.display.set_mode((x,y), SRCALPHA | extra )
        self.run()

    def run(self):
        running = True
        while running:
            running = self.update(self.currentFrameTime - self.lastFrameTime)
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.lastFrameTime = self.currentFrameTime
            self.currentFrameTime = time.clock()
            self.present()
        pygame.quit()
        print "quitting"
        sys.exit()

    def present(self):
        pygame.display.update()
        self.fpsClock.tick(50)
