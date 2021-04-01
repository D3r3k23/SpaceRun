
import Screen
import Resources

import pygame

imgs = Resources.images['Explosion']

FRAME_INT = 0.08 # Frame interval for animation in seconds

class Explosion(Screen.Drawable):
    def __init__(self, x, y):
        self.sinceLastFrame = 0
        self.frameNum = 0
        self.active = True

        super().__init__(imgs[0], x, y, center=True)
    
    def draw(self):
        if self.active:
            super().draw()
    
    # Check if animation should move to next frame
    def update(self, ts):
        if self.active:
            self.sinceLastFrame += ts
            if self.sinceLastFrame >= FRAME_INT:
                self.next_frame()

    def next_frame(self):
        self.sinceLastFrame = 0
        self.frameNum += 1

        if self.frameNum < len(imgs):
            self.img = imgs[self.frameNum]
        else:
            self.active = False
