import pygame
import math
import computation

class Bullet:

    timeTravelled = 0
    orientation = 0
    coordinate = (0,0)
    firedBy = -1

    def __init__(self, orientation, coordinate, firedBy):
        self.orientation = orientation
        self.coordinate = coordinate
        self.firedBy = firedBy

        self.updateCoordinate(30)

    def updateCoordinate(self, unitDistance):
        deg, x, y = computation.getDirection(self.orientation)
        self.coordinate = (self.coordinate[0] + (x * unitDistance * math.cos(math.radians(deg))) , self.coordinate[1] + (y * unitDistance * math.sin(math.radians(deg))) )

class Tank:
    # position of the tank
    coordinate = (0,0)

    # the image to display for this tank
    imageFile = ""

    fixedCursor = ""
    mobileCursor = ""

    center = 0

    # current orientation of the tank
    orientation = 0

    # the base rectangle for a tank
    rectangle = ""

    # amount of life for a tank
    life = 100

    # boost of this tank
    boost = 50

    # life bar for this tank
    lifeBar = ""

    # boost bar for this tank
    boostBar = ""

    # multiplier to get direction of movement for a tank
    reverse = 1

    def __init__(self, (X, Y), imageFile, orientation, life, boost, lifeBarX, lifeBarY, lifeBarW, lifeBarH, boostBarX, boostBarY, boostBarW, boostBarH):

        self.coordinate = (X,Y)
        self.imageFile = imageFile
        self.orientation = orientation
        self.life = life
        self.boost = boost
        self.lifeBar = pygame.Rect(lifeBarX, lifeBarY, lifeBarW, lifeBarH)
        self.boostBar = pygame.Rect(boostBarX, boostBarY, boostBarW, boostBarH)
        self.fixedCursor = pygame.image.load(self.imageFile)
        self.mobileCursor = self.fixedCursor
        self.mobileCursor =  pygame.transform.rotate(self.fixedCursor, self.orientation)
        self.rectangle = pygame.rect

    def rotateAntiClockwise(self, offset):
        self.orientation += offset + 360
        self.orientation %= 360
        self.updateMobileCursor()

    def rotateClockwise(self, offset):
        self.orientation -= offset + 360
        self.orientation %= 360
        self.updateMobileCursor()

    def updateMobileCursor(self):
        self.mobileCursor = pygame.transform.rotate(self.fixedCursor, self.orientation)

    def updateCenter(self):
        deg, x, y = computation.getDirection(self.orientation)
        self.center = self.mobileCursor.get_rect().center
        self.center = (self.center[0] + self.coordinate[0], self.center[1] + self.coordinate[1])

    def updateCoordinate(self, isBoost, unitDistance):
        deg, x, y = computation.getDirection(self.orientation)

        boostVal = 1
        if isBoost == 1:
            boostVal = 10

        self.coordinate = (self.coordinate[0] + (x * self.reverse * boostVal * unitDistance * math.cos( math.radians(deg) ) ) , self.coordinate[1] + (y * self.reverse * boostVal * unitDistance * math.sin( math.radians(deg) ) ) )

    def toggleReverse(self):
        if self.reverse == 1:
            self.reverse = -1
        else:
            self.reverse = 1

