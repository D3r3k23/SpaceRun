
import Screen
import Resources

import pygame

imgs = Resources.images['Exhaust']
for i, img in enumerate(imgs):
    imgs[i] = pygame.transform.scale(img, (56, 56))

FRAME_INT = 0.24

class Exhaust(Screen.Drawable):
    def __init__(self, spaceshipRect):
        self.spaceshipRect = spaceshipRect
        self.frameInt = 0.1 # Frame interval for animation in seconds

        self.sinceLastFrame = 0
        self.frameNum = 0
        self.active = True

        x, y = Exhaust.get_coord(spaceshipRect)
        super().__init__(imgs[0], x, y, center=True)
    
    # Check if animation should move to next frame, update position
    def update(self, ts, spaceshipRect, spaceshipSpeed):
        self.sinceLastFrame += ts
        if self.sinceLastFrame >= FRAME_INT / (spaceshipSpeed * 2):
            self.next_frame()
    
        x, y = Exhaust.get_coord(spaceshipRect)
        self.rect.centery = y
    
    @staticmethod
    def get_coord(spaceshipRect):
        return (spaceshipRect.left - 15, spaceshipRect.centery)

    def next_frame(self):
        self.sinceLastFrame = 0
        self.frameNum += 1
        if self.frameNum == len(imgs):
            self.frameNum = 0
        
        self.img = imgs[self.frameNum]
