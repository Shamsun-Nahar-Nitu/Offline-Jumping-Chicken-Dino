
# Obstacle Module

import pygame
import random
from game_config import *


class Obstacle:

    def __init__(self, x, obstacle_type):
 
        self.x = x
        self.type = obstacle_type
        
        # Set dimensions based on type
        if obstacle_type == 'small':
            self.width = 20
            self.height = 40
        elif obstacle_type == 'medium':
            self.width = 30
            self.height = 60
        else:  # large
            self.width = 40
            self.height = 70
        
        # Y position (on the ground)
        self.y = GROUND_Y - self.height
        
        # Create the cactus sprite
        self.sprite = self.create_cactus()
    
    def create_cactus(self):

        surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        cactus_color = (50, 150, 50)  # Green color
        
        # Draw main cactus body (vertical rectangle)
        main_width = self.width // 2
        pygame.draw.rect(surface, cactus_color, 
                        (self.width // 2 - main_width // 2, 0, main_width, self.height))
        
        # Add arms to cactus (if not small)
        if self.type != 'small':
            # Left arm
            arm_height = self.height // 3
            pygame.draw.rect(surface, cactus_color, 
                           (2, arm_height, main_width - 4, main_width // 2))
            
            # Right arm
            pygame.draw.rect(surface, cactus_color, 
                           (self.width - main_width + 2, arm_height + 10, 
                            main_width - 4, main_width // 2))
        
        return surface
    
    def update(self, speed):

        self.x -= speed
    
    def draw(self, screen):
 
        screen.blit(self.sprite, (self.x, self.y))
    
    def get_rect(self):
  
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def is_off_screen(self):
  
        return self.x + self.width < 0


class ObstacleManager:

    # Manages all obstacles in the game

    
    def __init__(self):
        # Initialize the obstacle manager
        self.obstacles = []  # List to store all active obstacles
        self.spawn_timer = 0  # Counts frames until next spawn
        self.next_spawn_distance = random.randint(MIN_OBSTACLE_DISTANCE, 
                                                   MAX_OBSTACLE_DISTANCE)
    
    def update(self, speed):
        
        #Update all obstacles
        

        # Update spawn timer
        self.spawn_timer += speed
        
        # Spawn new obstacle if it's time
        if self.spawn_timer >= self.next_spawn_distance:
            self.spawn_obstacle()
            self.spawn_timer = 0
            # Randomize next spawn distance
            self.next_spawn_distance = random.randint(MIN_OBSTACLE_DISTANCE, 
                                                       MAX_OBSTACLE_DISTANCE)
        
        # Update each obstacle
        for obstacle in self.obstacles:
            obstacle.update(speed)
        
        # Remove obstacles that are off screen
        self.obstacles = [obs for obs in self.obstacles if not obs.is_off_screen()]
    
    def spawn_obstacle(self):
        
        # Create a new obstacle off the right side of screen
        
        # Randomly choose obstacle type
        obstacle_type = random.choice(['small', 'medium', 'large'])
        
        # Create obstacle just off screen to the right
        new_obstacle = Obstacle(SCREEN_WIDTH, obstacle_type)
        self.obstacles.append(new_obstacle)
    
    def draw(self, screen):
 
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def check_collision(self, chicken_rect):
  
        for obstacle in self.obstacles:
            if chicken_rect.colliderect(obstacle.get_rect()):
                return True
        return False
    
    def reset(self):
        
        # Clear all obstacles (for game restart)
        
        self.obstacles = []
        self.spawn_timer = 0
        self.next_spawn_distance = random.randint(MIN_OBSTACLE_DISTANCE, 
                                                   MAX_OBSTACLE_DISTANCE)