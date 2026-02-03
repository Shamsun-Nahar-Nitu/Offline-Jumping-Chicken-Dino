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
    clock = pygame.time.Clock()
    
    chicken = Chicken()
    obstacles = ObstacleManager()
    ground = Ground()
    clouds = CloudManager()
    score = Score()
    
    game_active = True
    game_speed = INITIAL_GAME_SPEED

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    chicken.jump()

        if game_active:
            chicken.update()
            obstacles.update(game_speed)
            ground.update(game_speed)
            clouds.update()
            score.update(game_speed)
            game_speed += SPEED_INCREMENT

            if obstacles.check_collision(chicken.get_rect()):
                game_active = False # Game pauses on hit

            # --- DAY/NIGHT LOGIC ---
            curr = score.get_score()
            # Switches every 500 points
            if (curr // 500) % 2 == 1:
                bg_color, txt_color = NIGHT_COLOR, WHITE
            else:
                bg_color, txt_color = WHITE, BLACK

            screen.fill(bg_color)
            clouds.draw(screen)
            ground.draw(screen)
            obstacles.draw(screen)
            chicken.draw(screen)
            score.draw(screen, txt_color)
            
            pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()