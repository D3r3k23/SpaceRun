
import Screen
import Colors

import pygame

class GameObject(Screen.Drawable):
    SHOW_HITBOXES = False

    def __init__(self, img, x, y):
        super().__init__(img, x, y)
        self.mask = pygame.mask.from_surface(img)
        
        if GameObject.SHOW_HITBOXES:
            maskOutline = self.mask.outline()
            self.hitboxImg = self.img.copy()
            for point in maskOutline:
                pygame.draw.circle(self.hitboxImg, Colors.WHITE, point, 1)
    
    def draw(self):
        super().draw()
        if GameObject.SHOW_HITBOXES:
            Screen.Drawable(self.hitboxImg, self.rect.centerx, self.rect.centery).draw()
    
    @staticmethod
    def collision(obj1, obj2):
        if obj1.rect.colliderect(obj2.rect):
            offset = GameObject.get_mask_offset(obj1, obj2)
            return obj1.mask.overlap(obj2.mask, offset) is not None
        else:
            return False

    @staticmethod
    def get_mask_offset(obj1, obj2):
        return (
            obj2.rect.x - obj1.rect.x,
            obj2.rect.y - obj1.rect.y
        )
