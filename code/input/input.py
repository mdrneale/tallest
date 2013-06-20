import pygame
from pygame.locals import *

class Input:
    class __impl:
        def __init__(self):
            self.currentKeys    = pygame.key.get_pressed()
            self.lastKeys       = self.currentKeys

        def update(self):
            self.lastKeys       = self.currentKeys
            self.currentKeys    = pygame.key.get_pressed()

        def isKeyJustDown(self, keyName):
            return (self.currentKeys[keyName] and self.lastKeys[keyName] == False)

        def isKeyJustUp(self, keyName):
            return ((self.currentKeys[keyName] == False) and self.lastKeys[keyName])

        def isKeyDown(self, keyName):
            return self.currentKeys[keyName]

        def isKeyUp(self, keyName):
            return self.currentKeys[keyName] == False
 
     __instance = None
    def __init__(self):
        if MessageSystem.__instance is None:
            MessageSystem.__instance = MessageSystem.__impl()
        self.__dict__['_MessageSystem__instance'] = MessageSystem.__instance

    def __getattr__(self, attr):
        """ Delegate access to implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)
