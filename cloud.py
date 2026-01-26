# clouds in the background

import pygame
import random
from game_config import *


class Cloud:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.width = random.randint(40, 80)  # Random cloud size
        self.height = random.randint(20, 30)
        
        # Create the cloud sprite
        self.sprite = self.create_cloud_sprite()
    
    def create_cloud_sprite(self):

        surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        
        # Draw cloud as overlapping circles
        num_circles = random.randint(3, 5)
        for i in range(num_circles):
            x_pos = random.randint(5, self.width - 15)
            y_pos = random.randint(5, self.height - 10)
            radius = random.randint(8, 15)
            pygame.draw.circle(surface, CLOUD_GRAY, (x_pos, y_pos), radius)
        
        return surface
    
    def update(self):

        self.x -= CLOUD_SPEED
    
    def draw(self, screen):

        screen.blit(self.sprite, (self.x, self.y))
    
    def is_off_screen(self):

        return self.x + self.width < 0


class CloudManager:

    
    def __init__(self):

        self.clouds = []  # List of all active clouds
        self.spawn_timer = 0
        self.next_spawn_distance = random.randint(MIN_CLOUD_DISTANCE, 
                                                   MAX_CLOUD_DISTANCE)
        
        # Create a few initial clouds
        for i in range(3):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(30, 150)
            self.clouds.append(Cloud(x, y))
    
    def update(self):

        # Update spawn timer
        self.spawn_timer += CLOUD_SPEED
        
        # Spawn new cloud if it's time
        if self.spawn_timer >= self.next_spawn_distance:
            self.spawn_cloud()
            self.spawn_timer = 0
            self.next_spawn_distance = random.randint(MIN_CLOUD_DISTANCE, 
                                                       MAX_CLOUD_DISTANCE)
        
        # Update each cloud
        for cloud in self.clouds:
            cloud.update()
        
        # Remove clouds that are off screen
        self.clouds = [cloud for cloud in self.clouds if not cloud.is_off_screen()]
    
    def spawn_cloud(self):

        # Random y position in the sky
        y = random.randint(30, 150)
        new_cloud = Cloud(SCREEN_WIDTH, y)
        self.clouds.append(new_cloud)
    
    def draw(self, screen):

        for cloud in self.clouds:
            cloud.draw(screen)
    
    def reset(self):

        self.clouds = []
        self.spawn_timer = 0
        self.next_spawn_distance = random.randint(MIN_CLOUD_DISTANCE, 
                                                   MAX_CLOUD_DISTANCE)
        
        # Create initial clouds
        for i in range(3):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(30, 150)
            self.clouds.append(Cloud(x, y))