
# Chicken Character Module


import pygame
from game_config import *


class Chicken:   
    def __init__(self):
        # Position
        self.x = CHICKEN_X
        self.y = GROUND_Y - 60  # Start on the ground
        self.width = 44
        self.height = 60
        
        # Physics
        self.velocity_y = 0  # Vertical speed (positive = falling, negative = jumping)
        self.is_jumping = False
        
        # Animation
        self.animation_frame = 0
        self.animation_counter = 0
        
        # Create pixel art chicken sprite
        self.create_chicken_sprite()
    
    def create_chicken_sprite(self):
        # Create two frames for running animation
        self.sprites = []
        
        # Frame 1 - Chicken standing
        sprite1 = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.draw_chicken(sprite1, leg_forward=True)
        self.sprites.append(sprite1)
        
        # Frame 2 - Chicken with other leg forward
        sprite2 = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.draw_chicken(sprite2, leg_forward=False)
        self.sprites.append(sprite2)
    
    def draw_chicken(self, surface, leg_forward):
        # Colors for the chicken
        body_color = (255, 200, 100)  # Orange-yellow body
        beak_color = (255, 165, 0)    # Orange beak
        eye_color = BLACK
        comb_color = (255, 0, 0)      # Red comb
        leg_color = (255, 165, 0)     # Orange legs
        
        # Draw body 
        # Body is positioned in the middle-upper part
        pygame.draw.ellipse(surface, body_color, (6, 20, 30, 25))
        
        # Draw head
        pygame.draw.circle(surface, body_color, (32, 15), 8)
        
        # Draw comb
        comb_points = [(30, 8), (32, 4), (34, 8)]
        pygame.draw.polygon(surface, comb_color, comb_points)
        
        # Draw eye 
        pygame.draw.circle(surface, eye_color, (34, 14), 2)
        
        # Draw beak 
        beak_points = [(39, 16), (42, 15), (39, 14)]
        pygame.draw.polygon(surface, beak_color, beak_points)
        
        # Draw tail 
        pygame.draw.polygon(surface, body_color, [(9, 28), (2, 25), (6, 32)])
        pygame.draw.polygon(surface, body_color, [(9, 32), (2, 30), (6, 36)])
        
        # Draw legs 
        if leg_forward:
            # Left leg forward
            pygame.draw.rect(surface, leg_color, (18, 45, 3, 12))
            # Right leg back
            pygame.draw.rect(surface, leg_color, (28, 45, 3, 12))
        else:
            # Right leg forward
            pygame.draw.rect(surface, leg_color, (28, 45, 3, 12))
            # Left leg back
            pygame.draw.rect(surface, leg_color, (18, 45, 3, 12))
        
        # Draw feet 
        if leg_forward:
            pygame.draw.rect(surface, leg_color, (16, 57, 6, 2))
            pygame.draw.rect(surface, leg_color, (26, 57, 6, 2))
        else:
            pygame.draw.rect(surface, leg_color, (26, 57, 6, 2))
            pygame.draw.rect(surface, leg_color, (16, 57, 6, 2))
    
    def jump(self):
        if not self.is_jumping:
            self.velocity_y = JUMP_STRENGTH
            self.is_jumping = True
    
    def update(self):

        # Apply gravity
        self.velocity_y += GRAVITY
        self.y += self.velocity_y
        
        # Check if chicken landed on ground
        if self.y >= GROUND_Y - self.height:
            self.y = GROUND_Y - self.height
            self.velocity_y = 0
            self.is_jumping = False
        
        # Update running animation 
        if not self.is_jumping:
            self.animation_counter += 1
            if self.animation_counter >= 10:  # Change frame every 10 updates
                self.animation_counter = 0
                self.animation_frame = (self.animation_frame + 1) % 2
    
    def draw(self, screen):
        # Use the current animation frame
        current_sprite = self.sprites[self.animation_frame]
        screen.blit(current_sprite, (self.x, self.y))
    
    def get_rect(self):

        # Make hitbox smaller
        return pygame.Rect(self.x + 5, self.y + 5, self.width - 10, self.height - 10)