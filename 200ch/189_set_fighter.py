import pygame, os, sys

DESTIN_DIR = os.path.dirname(__file__)+'/sprites/Galaga/'

BLACK = (0,0,0)
PAD_WIDTH = 480
PAD_HEIGHT = 640

FIGHTER_WIDTH = 36
FIGHTER_HEIGHT = 38

DICT_OBJ = {
    'fighter' : [36, 38, (PAD_WIDTH - 36)/2, PAD_HEIGHT-(36+10), 'Ship_White.png'],
    'g_catcher' : [36, 38, 200, 100, 'Green_Catcher.png'],
    'gremlin'   : [36, 38, 200, 150, 'gremlin_0001.png'],
    'bee'       : [36, 38, 200, 200, 'Fly_0001.png'],
    'scorpion'  : [36, 38, 200, 250, 'scorpion_0001.png'],
    'phoenix'   : [36, 38, 200, 300, 'phoenix_0001.png'],
    'bullit'    : [13, 22, 200, 500, 'rocket_0001.png'],
}

DISPLAYSURF = pygame.display.set_mode((PAD_WIDTH, PAD_HEIGHT))
pygame.display.set_caption('My Galaga')
clock = pygame.time.Clock()

def set_image(filename):
    return pygame.image.load(DESTIN_DIR + filename)

def set_size(obj, width, height):
    return pygame.transform.scale(obj, (width, height))

def draw_object(obj, x, y):
    DISPLAYSURF.blit(obj, (x, y))

def run_game():
    x = PAD_WIDTH * 0.45
    y = PAD_HEIGHT - (FIGHTER_HEIGHT + 10)

    x_change = 0
    y_change = 0

    ongame = False

    while not ongame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ongame = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5

                elif event.key == pygame.K_RIGHT:
                    x_change = +5

                elif event.key == pygame.K_UP:
                    y_change = -5

                elif event.key == pygame.K_DOWN:
                    y_change = +5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        x += x_change
        y += y_change

        if x < 0:
            x = 0
        elif x > PAD_WIDTH - FIGHTER_WIDTH:
            x = PAD_WIDTH - FIGHTER_WIDTH

        if y < 0:
            y = 0
        elif y > PAD_HEIGHT - FIGHTER_HEIGHT:
            y = PAD_HEIGHT - FIGHTER_HEIGHT

        DISPLAYSURF.fill(BLACK)

        draw_object(fighter, x, y)
        draw_object(gremlin, DICT_OBJ['gremlin'][2], DICT_OBJ['gremlin'][3])
        draw_object(bee, DICT_OBJ['bee'][2], DICT_OBJ['bee'][3])

        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    sys.exit()

def init_game():
    global gamepad, clock

    pygame.init()
    gamepad = pygame.display.set_mode((PAD_WIDTH, PAD_HEIGHT))
    pygame.display.set_caption('My Galaga')
    clock = pygame.time.Clock()

fighter = set_image(DICT_OBJ['fighter'][4])
fighter = set_size(fighter, DICT_OBJ['fighter'][0], DICT_OBJ['fighter'][1])

gremlin = set_image(DICT_OBJ['gremlin'][4])
gremlin = set_size(gremlin, DICT_OBJ['gremlin'][0], DICT_OBJ['gremlin'][1])

bee = set_image(DICT_OBJ['bee'][4])
bee = set_size(bee, DICT_OBJ['bee'][0], DICT_OBJ['bee'][1])

init_game()
run_game()
