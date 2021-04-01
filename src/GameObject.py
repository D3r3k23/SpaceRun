
import Screen
import Colors

import pygame

class GameObject(Screen.Drawable):
    SHOW_HITBOXES = False # Not very useful anymore

    def __init__(self, img, x, y): # center coordinates
        super().__init__(img, x, y, center=True)
        self.mask = pygame.mask.from_surface(img) # Mask of the opaque area of image
        
        if GameObject.SHOW_HITBOXES:
            maskOutline = self.mask.outline()
            hitboxImg = self.img.copy()
            for point in maskOutline:
                pygame.draw.circle(hitboxImg, Colors.WHITE, point, 1)

            self.hitbox = Screen.Drawable(hitboxImg, 0, 0, center=True)
    
    def draw(self):
        super().draw()
        if GameObject.SHOW_HITBOXES: # Update hitbox rect and draw
            self.hitbox.rect.center = self.rect.center
            self.hitbox.draw()
    
    def move(self, dx, dy):
        self.rect.move(dx, dy)
    
    # Check two objects overlap using masks
    @staticmethod
    def collision(obj1, obj2):
        if obj1.rect.colliderect(obj2.rect):
            offset = GameObject.get_mask_offset(obj1, obj2)
            return obj1.mask.overlap(obj2.mask, offset) is not None
        else:
            return False

    # Get mask offset from each object's position
    @staticmethod
    def get_mask_offset(obj1, obj2):
        return (
            obj2.rect.x - obj1.rect.x,
            obj2.rect.y - obj1.rect.y
        )
