# Main Game File

import pygame
import sys
from game_config import *
from chicken import Chicken
from obstacle import ObstacleManager
from ground import Ground
from cloud import CloudManager
from score import Score


def initialize_game():

    # Initialize all pygame modules
    pygame.init()
    
    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Chicken Runner - Press SPACE to Jump!")
    
    # Create a clock to control frame rate
    clock = pygame.time.Clock()
    
    return screen, clock


def show_start_screen(screen):

    # Clear screen
    screen.fill(WHITE)
    
    # Create text
    title_font = pygame.font.Font(None, 60)
    instruction_font = pygame.font.Font(None, 30)
    
    title_text = title_font.render("CHICKEN RUNNER", True, BLACK)
    instruction_text = instruction_font.render("Press SPACE to Start", True, GRAY)
    jump_text = instruction_font.render("Press SPACE to Jump", True, GRAY)
    
    # Position text in center
    screen.blit(title_text, (SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 - 80))
    screen.blit(instruction_text, (SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2))
    screen.blit(jump_text, (SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2 + 40))
    
    pygame.display.flip()


def show_game_over_screen(screen, final_score, high_score):

    font_large = pygame.font.Font(None, 50)
    font_medium = pygame.font.Font(None, 35)
    font_small = pygame.font.Font(None, 25)
    
    game_over_text = font_large.render("GAME OVER", True, BLACK)
    score_text = font_medium.render(f"Score: {final_score:05d}", True, BLACK)
    restart_text = font_small.render("Press SPACE to Restart", True, GRAY)
    
    # Show high score if applicable
    if high_score > 0:
        high_score_text = font_medium.render(f"High Score: {high_score:05d}", True, GRAY)
        screen.blit(high_score_text, (SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 - 10))
    
    # Position text
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2 - 80))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT // 2 + 30))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - 140, SCREEN_HEIGHT // 2 + 80))
    
    pygame.display.flip()


def reset_game():
    # Create new game objects
    chicken = Chicken()
    obstacles = ObstacleManager()
    ground = Ground()
    clouds = CloudManager()
    score = Score()
    game_speed = INITIAL_GAME_SPEED
    
    return chicken, obstacles, ground, clouds, score, game_speed


def main():
    # Set up the game
    screen, clock = initialize_game()
    
    # Create game objects
    chicken, obstacles, ground, clouds, score, game_speed = reset_game()
    
    # Game state variables
    game_active = False  # Is the game currently running?
    waiting_for_start = True  # Waiting for player to start?
    
    # Show start screen
    show_start_screen(screen)
    
    # Main game loop - runs until player closes window
    running = True
    while running:
        
        # EVENT HANDLING - Check for player input
        for event in pygame.event.get():
            # Player clicked the X button
            if event.type == pygame.QUIT:
                running = False
            
            # Player pressed a key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Starting the game for first time
                    if waiting_for_start:
                        waiting_for_start = False
                        game_active = True
                    
                    # Restarting after game over
                    elif not game_active:
                        chicken, obstacles, ground, clouds, score, game_speed = reset_game()
                        game_active = True
                    
                    # Jump during active game
                    elif game_active:
                        chicken.jump()
        
        # GAME LOGIC - Only update if game is active
        if game_active:
            # Update all game objects
            chicken.update()
            obstacles.update(game_speed)
            ground.update(game_speed)
            clouds.update()
            score.update(game_speed)
            
            # Increase game speed gradually (gets harder over time)
            game_speed += SPEED_INCREMENT
            
            # Check for collision with obstacles
            if obstacles.check_collision(chicken.get_rect()):
                game_active = False
                score.reset()  # This also updates high score
                show_game_over_screen(screen, score.get_score(), score.high_score)
        
        # RENDERING - Draw everything (only if game is active)
        if game_active:
            # Clear screen with white background
            screen.fill(WHITE)
            
            # Draw all game elements (order matters - back to front)
            clouds.draw(screen)  # Draw clouds first (background)
            ground.draw(screen)  # Draw ground
            obstacles.draw(screen)  # Draw obstacles
            chicken.draw(screen)  # Draw chicken on top
            score.draw(screen)  # Draw score last (always on top)
            
            # Update the display
            pygame.display.flip()
        
        # Control frame rate (60 FPS)
        clock.tick(FPS)
    
    # Clean up and quit
    pygame.quit()
    sys.exit()


# This runs when you execute this file
if __name__ == "__main__":
    main()