import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


ball_radius = 15
ball_speed = [5, 5]

paddle_width, paddle_height = 10, 100
player_speed = 10
opponent_speed = 7

# Ball position
ball = pygame.Rect(WIDTH//2 - ball_radius, HEIGHT//2 - ball_radius, ball_radius*2, ball_radius*2)

# Paddles
player = pygame.Rect(WIDTH - 20, HEIGHT//2 - paddle_height//2, paddle_width, paddle_height)
opponent = pygame.Rect(10, HEIGHT//2 - paddle_height//2, paddle_width, paddle_height)

# Scores
player_score = 0
opponent_score = 0
font = pygame.font.SysFont("comicsans", 40)
clock = pygame.time.Clock()

while True:
    screen.fill(BLACK)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= player_speed
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += player_speed

    # -------------------- Opponent AI -------------------- #
    if opponent.centery < ball.centery:
        opponent.y += opponent_speed
    if opponent.centery > ball.centery:
        opponent.y -= opponent_speed
    # Keep opponent in screen
    if opponent.top < 0:
        opponent.top = 0
    if opponent.bottom > HEIGHT:
        opponent.bottom = HEIGHT

    # -------------------- Ball Movement -------------------- #
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Collisions with top/bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Collisions with paddles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed[0] = -ball_speed[0]

    # Score update
    if ball.left <= 0:
        player_score += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed = [5, 5]
    if ball.right >= WIDTH:
        opponent_score += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed = [-5, 5]

    # -------------------- Draw Objects -------------------- #
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    # Draw Scores
    player_text = font.render(f"{player_score}", True, WHITE)
    opponent_text = font.render(f"{opponent_score}", True, WHITE)
    screen.blit(player_text, (WIDTH//2 + 20, 20))
    screen.blit(opponent_text, (WIDTH//2 - 40, 20))

    # Update Display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS
