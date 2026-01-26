#Chicken Character Module


import pygame
from game_config import *


class Chicken:
    # The main player character

    
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
        """
        Draw a pixel art chicken on the given surface
        
        Args:
            surface: The pygame surface to draw on
            leg_forward: Boolean to determine which leg is forward (for animation)
        """
        # Colors for the chicken
        body_color = (255, 200, 100)  # Orange-yellow body
        beak_color = (255, 165, 0)    # Orange beak
        eye_color = BLACK
        comb_color = (255, 0, 0)      # Red comb
        leg_color = (255, 165, 0)     # Orange legs
        
        # Draw body (main oval shape)
        # Body is positioned in the middle-upper part
        pygame.draw.ellipse(surface, body_color, (8, 20, 30, 25))
        
        # Draw head (smaller circle)
        pygame.draw.circle(surface, body_color, (12, 15), 8)
        
        # Draw comb (red thing on top of head)
        comb_points = [(10, 8), (12, 4), (14, 8)]
        pygame.draw.polygon(surface, comb_color, comb_points)
        
        # Draw eye (small black dot)
        pygame.draw.circle(surface, eye_color, (10, 14), 2)
        
        # Draw beak (small triangle)
        beak_points = [(5, 16), (2, 15), (5, 14)]
        pygame.draw.polygon(surface, beak_color, beak_points)
        
        # Draw tail feathers (pointed back)
        pygame.draw.polygon(surface, body_color, [(35, 28), (42, 25), (38, 32)])
        pygame.draw.polygon(surface, body_color, [(35, 32), (42, 30), (38, 36)])
        
        # Draw legs - position changes based on animation
        if leg_forward:
            # Left leg forward
            pygame.draw.rect(surface, leg_color, (15, 45, 3, 12))
            # Right leg back
            pygame.draw.rect(surface, leg_color, (25, 45, 3, 12))
        else:
            # Right leg forward
            pygame.draw.rect(surface, leg_color, (25, 45, 3, 12))
            # Left leg back
            pygame.draw.rect(surface, leg_color, (15, 45, 3, 12))
        
        # Draw feet (small rectangles at bottom of legs)
        if leg_forward:
            pygame.draw.rect(surface, leg_color, (13, 57, 6, 2))
            pygame.draw.rect(surface, leg_color, (23, 57, 6, 2))
        else:
            pygame.draw.rect(surface, leg_color, (23, 57, 6, 2))
            pygame.draw.rect(surface, leg_color, (13, 57, 6, 2))
    
    def jump(self):
        """
        Make the chicken jump if it's on the ground
        """
        if not self.is_jumping:
            self.velocity_y = JUMP_STRENGTH
            self.is_jumping = True
    
    def update(self):
        """
        Update chicken position and physics each frame
        """
        # Apply gravity
        self.velocity_y += GRAVITY
        self.y += self.velocity_y
        
        # Check if chicken landed on ground
        if self.y >= GROUND_Y - self.height:
            self.y = GROUND_Y - self.height
            self.velocity_y = 0
            self.is_jumping = False
        
        # Update running animation (only when on ground)
        if not self.is_jumping:
            self.animation_counter += 1
            if self.animation_counter >= 10:  # Change frame every 10 updates
                self.animation_counter = 0
                self.animation_frame = (self.animation_frame + 1) % 2
    
    def draw(self, screen):
        """
        Draw the chicken on the screen
        
        Args:
            screen: The pygame screen surface to draw on
        """
        # Use the current animation frame
        current_sprite = self.sprites[self.animation_frame]
        screen.blit(current_sprite, (self.x, self.y))
    
    def get_rect(self):
        """
        Get the chicken's collision rectangle
        Returns a slightly smaller rect for better collision feel
        
        Returns:
            pygame.Rect: The collision box
        """
        # Make hitbox slightly smaller for fairer collision
        return pygame.Rect(self.x + 5, self.y + 5, self.width - 10, self.height - 10)