# Score Module

import pygame
from game_config import *


class Score:

    def __init__(self):
        self.score = 0  # Current score
        self.high_score = 0  # Best score achieved
        self.score_increment = 0  # Fractional score accumulator
        
        # Font for displaying score
        self.font = pygame.font.Font(None, 30)
    
    def update(self, speed):

        # Add a fraction to score based on speed
        # This makes score increase smoothly
        self.score_increment += speed * 0.1
        
        # When we've accumulated enough for a full point, add it
        if self.score_increment >= 1:
            self.score += int(self.score_increment)
            self.score_increment = self.score_increment - int(self.score_increment)
    
    def draw(self, screen):

        # Format score with leading zeros (like original game)
        score_text = self.font.render(f"{int(self.score):05d}", True, BLACK)
        
        # Draw in top right corner
        screen.blit(score_text, (SCREEN_WIDTH - 120, 20))
        
        # Draw high score if player has one
        if self.high_score > 0:
            high_score_text = self.font.render(f"HI {int(self.high_score):05d}", 
                                               True, GRAY)
            screen.blit(high_score_text, (SCREEN_WIDTH - 250, 20))
    
    def reset(self):

        # Update high score if we beat it
        if self.score > self.high_score:
            self.high_score = self.score
        
        # Reset current score
        self.score = 0
        self.score_increment = 0
    
    def get_score(self):

        return int(self.score)