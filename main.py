import pygame
import sys
from game_config import *
from chicken import Chicken
from obstacle import ObstacleManager
from ground import Ground
from cloud import CloudManager
from score import Score

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Offline Jumping Chicken")
    clock = pygame.time.Clock()
    
    # Initialize objects
    chicken = Chicken()
    obstacles = ObstacleManager()
    ground = Ground()
    clouds = CloudManager()
    score = Score()
    
    game_active = True
    game_speed = INITIAL_GAME_SPEED
    font = pygame.font.Font(None, 50)

    while True:
        # 1. EVENT HANDLING
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                # --- JUMP / RESTART LOGIC ---
                if event.key == pygame.K_SPACE:
                    if game_active:
                        chicken.jump()
                    else:
                        # RESTART LOGIC: Reset everything
                        game_active = True
                        obstacles.reset()
                        score.reset()
                        game_speed = INITIAL_GAME_SPEED

                # --- RESET HIGH SCORE LOGIC ---
                if event.key == pygame.K_r: # Press 'R' to reset high score
                    score.high_score = 0
                    score.save_high_score()

        # 2. UPDATE LOGIC (Only if game is running)
        if game_active:
            chicken.update()
            obstacles.update(game_speed)
            ground.update(game_speed)
            clouds.update()
            score.update(game_speed)
            game_speed += SPEED_INCREMENT

            if obstacles.check_collision(chicken.get_rect()):
                game_active = False # Triggers the "Game Over" state

        # 3. DRAWING LOGIC (Always draw, even if paused)
        curr = score.get_score()
        # Toggle Day/Night based on score (every 500 points)
        bg_color, txt_color = (NIGHT_COLOR, WHITE) if (curr // 500) % 2 == 1 else (WHITE, BLACK)
        
        screen.fill(bg_color)
        clouds.draw(screen)
        ground.draw(screen)
        obstacles.draw(screen)
        chicken.draw(screen)
        score.draw(screen, txt_color)

        # Show Game Over Message
        if not game_active:
            over_text = font.render("GAME OVER - Press SPACE", True, txt_color)
            text_rect = over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            screen.blit(over_text, text_rect)
            
            reset_hint = pygame.font.Font(None, 25).render("Press 'R' to Reset High Score", True, txt_color)
            hint_rect = reset_hint.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))
            screen.blit(reset_hint, hint_rect)
            
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()