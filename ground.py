# animates the scrolling ground


import pygame
from game_config import *


class Ground:
  
    def __init__(self):
        # Initialize the ground
        self.y = GROUND_Y  # Ground's vertical position
        
        # Create ground segments
        # two segments to create seamless scrolling
        self.width = SCREEN_WIDTH
        self.height = GROUND_HEIGHT
        
        # Position of first ground segment
        self.x1 = 0
        # Position of second ground segment (starts right after first)
        self.x2 = self.width
        
        # Create the ground sprite
        self.sprite = self.create_ground_sprite()
    
    def create_ground_sprite(self):
        surface = pygame.Surface((self.width, self.height))
        surface.fill(WHITE)
        
        # Draw ground line at the top
        pygame.draw.line(surface, BLACK, (0, 0), (self.width, 0), 2)
        
        # Add some small dashes for ground detail
        for i in range(0, self.width, 40):
            pygame.draw.line(surface, GRAY, (i, 5), (i + 20, 5), 1)
        
        return surface
    
    def update(self, speed):
        # Move both segments left
        self.x1 -= speed
        self.x2 -= speed
        
        # If first segment moves completely off screen
        if self.x1 + self.width <= 0:
            # Reset it to the right of the second segment
            self.x1 = self.x2 + self.width
        
        # If second segment moves completely off screen
        if self.x2 + self.width <= 0:
            # Reset it to the right of the first segment
            self.x2 = self.x1 + self.width
    
    def draw(self, screen):

        # Draw first segment
        screen.blit(self.sprite, (self.x1, self.y))
        # Draw second segment
        screen.blit(self.sprite, (self.x2, self.y))
    
    def reset(self):

        self.x1 = 0
        self.x2 = self.width