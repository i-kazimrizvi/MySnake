import pygame
import sys
import random

pygame.init()
background = pygame.display.set_mode((500, 500))

clock = pygame.time.Clock()
targetLocation = []
initDir = 'L'
nextDir = initDir
points = 0
targetAvailable = True
gameOver = False

# defining colours
colourRed = pygame.Color(255, 0, 0)
colourBlack = pygame.Color(0, 0, 0)
colourWhite = pygame.Color(255, 255, 255)
colourBrown = pygame.Color(165, 42, 42)
colourGreen = pygame.Color(0, 255, 0)

mySnakeBody = [[250, 250], [240, 250], [230, 250]]
mySnakeHead = [250, 250]


def insert_new_pos(head, body):
    body.insert(0, list(head))


def add_target_location():
    global targetLocation
    targetLocation = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]


def draw_snake_target(body, bg, black, green, target):
    for pos in body:
        pygame.draw.rect(bg, black, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(bg, green, pygame.Rect(target[0], target[1], 10, 10))


def finish():
    global gameOver
    gameOver = True


def check_collision_wall(head):
    if head[0] >= 500 or head[0] <= 0:
        finish()
    if head[1] >= 500 or head[1] <= 0:
        finish()


def check_collision_body(head, body):
    for i in body[1:]:
        if head[0] == i[0] and head[1] == i[1]:
            finish()


def display_score():
    global background
    font = pygame.font.SysFont('ubuntumono', 20)
    area = font.render('points : {0}'.format(points), True, colourBrown)
    area_points = area.get_rect()
    area_points.midtop = (100, 10)
    background.blit(area, area_points)


add_target_location()

while not gameOver:
    background.fill(colourBlack)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                nextDir = 'R'
            elif event.key == pygame.K_LEFT:
                nextDir = 'L'
            elif event.key == pygame.K_UP:
                nextDir = 'U'
            elif event.key == pygame.K_DOWN:
                nextDir = 'D'
            else:
                nextDir = initDir





        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    # cant turn in the opposite dir'n

    if nextDir == 'R' and not initDir == 'L':
        nextDir = 'R'

    elif nextDir == 'L' and not initDir == 'R':
        nextDir = 'L'

    elif nextDir == 'U' and not initDir == 'D':
        nextDir = 'U'

    elif nextDir == 'D' and not initDir == 'U':
        nextDir = 'D'
    else:
        nextDir = initDir

    #changing location of head based on input

    if nextDir == 'R':
        mySnakeHead[0] += 10
        initDir = nextDir

    if nextDir == 'L':
        mySnakeHead[0] -= 10
        initDir = nextDir

    if nextDir == 'U':
        mySnakeHead[1] -= 10
        initDir = nextDir

    if nextDir == 'D':
        mySnakeHead[1] += 10
        initDir = nextDir

    insert_new_pos(mySnakeHead, mySnakeBody)

    if mySnakeHead[0] == targetLocation[0] and targetLocation[1] == mySnakeHead[1]:
        points += 1
        add_target_location()
    else:
        mySnakeBody.pop()

    draw_snake_target(mySnakeBody, background, colourWhite, colourGreen, targetLocation)

    check_collision_wall(mySnakeHead)

    display_score()

    pygame.display.flip()

    clock.tick(40)
