import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
CELL = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()

def draw_snake(snake):
    for x, y in snake:
        pygame.draw.rect(screen, GREEN, (x, y, CELL, CELL))

def game_over():
    font = pygame.font.SysFont(None, 50)
    text = font.render("GAME OVER!", True, WHITE)
    screen.blit(text, (WIDTH//3, HEIGHT//3))
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

def main():
    x = WIDTH // 2
    y = HEIGHT // 2
    dx, dy = 0, 0

    snake = [(x, y)]
    length = 1

    # Food position
    food = (random.randrange(0, WIDTH, CELL),
            random.randrange(0, HEIGHT, CELL))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -CELL
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, CELL
                elif event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -CELL, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = CELL, 0

        # Move snake
        x += dx
        y += dy
        snake.append((x, y))

        if len(snake) > length:
            snake.pop(0)

        # Check collision with walls
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_over()

        # Check collision with self
        if len(snake) != len(set(snake)):
            game_over()

        # Check collision with food
        if (x, y) == food:
            length += 1
            food = (random.randrange(0, WIDTH, CELL),
                    random.randrange(0, HEIGHT, CELL))

        # Draw everything
        screen.fill(BLACK)
        draw_snake(snake)
        pygame.draw.rect(screen, RED, (food[0], food[1], CELL, CELL))
        pygame.display.update()

        clock.tick(10)  # Game speed

if __name__ == "__main__":
    main()
