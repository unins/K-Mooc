import pygame

BLACK = (0,0,0)
pad_width = 480
pad_height = 640

def run_game():
    global gamepad, clock

    done_flag = False
    while not done_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done_flag = True

        gamepad.fill(BLACK)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

def init_game():
    global gamepad, clock

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('My Galaga')
    clock = pygame.time.Clock()

init_game()
run_game()
