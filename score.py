import pygame
import os
from game_config import *

class Score:
    def __init__(self):
        self.score = 0
        self.score_increment = 0
        self.high_score = self.load_high_score()
        self.font = pygame.font.Font(None, 30)

    def load_high_score(self):
        if os.path.exists("highscore.txt"):
            try:
                with open("highscore.txt", "r") as f:
                    return int(f.read())
            except:
                return 0
        return 0

    def save_high_score(self):
        with open("highscore.txt", "w") as f:
            f.write(str(int(self.high_score)))

    def update(self, speed):
        self.score_increment += speed * 0.1
        if self.score_increment >= 1:
            self.score += int(self.score_increment)
            self.score_increment -= int(self.score_increment)
    
    def draw(self, screen, color=BLACK):
        score_text = self.font.render(f"{int(self.score):05d}", True, color)
        screen.blit(score_text, (SCREEN_WIDTH - 120, 20))
        if self.high_score > 0:
            high_score_text = self.font.render(f"HI {int(self.high_score):05d}", True, color)
            screen.blit(high_score_text, (SCREEN_WIDTH - 250, 20))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.score_increment = 0

    def get_score(self):
        return int(self.score) 