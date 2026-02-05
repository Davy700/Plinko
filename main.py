import pygame, sys, pymunk
from random import randint, choice
from program_tools import RenderText

pygame.init()
width = 800
height = 975
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('PLINKO')
clock = pygame.time.Clock()

class Apple():
    def __init__(self, space, pos, k, bet):
        self.body = pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC)
        self.body.position = pos
        self.shape = pymunk.Circle(self.body, 15)
        self.shape.collision_type = k
        self.bet = bet
        space.add(self.body, self.shape)
        self.collision = [self.collide1, self.collide2, self.collide3, self.collide4, self.collide5, self.collide6, self.collide7, self.collide8, self.collide9]

    def collide1(self, arbiter, space, data):
        global money
        self.body.position = (10000,10000)
        self.bet  = self.bet * 2
        money += self.bet

        return True

    def collide2(self, arbiter, space, data):
        global money
        self.body.position = (10000,10000)
        self.bet  = self.bet * 1.5
        money += self.bet

        return True

    def collide3(self, arbiter, space, data):
        global money
        self.body.position = (10000,10000)
        self.bet  = self.bet * 1
        money += self.bet

        return True

    def collide4(self, arbiter, space, data):
        global money
        self.body.position = (10000,10000)
        self.bet  = self.bet * 0.5
        money += self.bet

        return True

    def collide5(self, arbiter, space, data):
        global money
        self.body.position = (10000,10000)
        self.bet  = self.bet * 0.25
        money += self.bet

        return True

    def collide6(self, arbiter, space, data):
        global money
        self.body.position = (10000,10000)
        self.bet  = self.bet * 0.5
        money += self.bet

        return True

    def collide7(self, arbiter, space, data):
        global money
        self.body.position = (10000,10000)
        self.bet  = self.bet * 1
        money += self.bet

        return True

    def collide8(self, arbiter, space, data):
        global money
        self.body.position = (10000,10000)
        self.bet  = self.bet * 1.5
        money += self.bet

        return True

    def collide9(self, arbiter, space, data):
        global money
        self.body.position = (10000,10000)
        self.bet  = self.bet * 2
        money += self.bet

        return True


def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        pygame.draw.circle(win, (255,80,80), (pos_x, pos_y), 15)

def static_ball(space, pos):
    body = pymunk.Body(body_type= pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body,10)
    space.add(body, shape)
    return shape

def draw_static_ball(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(win, (255,255,255), (pos_x, pos_y), 10)


def multiplier(space, positions):
    l = []
    for i in range(len(positions)):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = positions[i]
        shape = pymunk.Poly.create_box(body, (40,20))
        space.add(body, shape)
        shape.collision_type = i+1
        l.append(shape)
    return l

def draw_multiplier(multipliers):
    for multiplier in multipliers:
        pos_x = int(multiplier.body.position.x)
        pos_y = int(multiplier.body.position.y)
        pygame.draw.rect(win, (0,255,0), (pos_x-20, pos_y-10, 40, 20))

money = 100

space = pymunk.Space()
space.gravity = (0,500)

apples = []
multiplier_pos = [
    (160,900),(220,900),(280,900),(340,900),(400,900),(460,900),(520,900),(580,900),(640,900)
]
multipliers = multiplier(space, multiplier_pos)

title_size = 15
title_color = (25,25,25)
multipliers_title = [
                     RenderText(f'2×', title_size, title_color),
                     RenderText(f'1.5×', title_size, title_color),
                     RenderText(f'1×', title_size, title_color),
                     RenderText(f'0.5×', title_size, title_color),
                     RenderText(f'0.25×', title_size, title_color),
                     RenderText(f'0.5×', title_size, title_color),
                     RenderText(f'1×', title_size, title_color),
                     RenderText(f'1.5×', title_size, title_color),
                     RenderText(f'2×', title_size, title_color)
                    ]

multiplier_rect = []

for i, text in enumerate(multipliers_title):
    a = text.get_rect(center=multiplier_pos[i])
    multiplier_rect.append(a)


balls = []
balls_pos = [
    (85, 775), (155,775), (225,775), (295,775), (365,775), (435,775), (505,775), (575,775), (645,775), (715,775),
    (120, 680), (190,680), (260,680), (330,680), (400,680), (470,680), (540,680), (610,680), (680,680),
    (155,575), (225,575), (295,575), (365,575), (435,575), (505,575), (575,575), (645, 575),
    (190,490), (260,490), (330,490), (400,490), (470,490), (540,490), (610,490),
    (225,395), (295,395), (365,395), (435,395), (505,395), (575,395),
    (260, 300), (330, 300), (400, 300), (470, 300), (540, 300),
    (295,215), (365,215), (435,215), (505,215),
    (330, 110), (400, 110), (470, 110),
]

for i in balls_pos:
    balls.append(static_ball(space, i))

countdown = 0
bet_countdown = 0
keys = pygame.key.get_pressed()

k = 10
handlers = [[],[],[],[],[],[],[],[],[]]
bet = 10

run = True
while run:
    win.fill((50,50,50))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            run = False

    if keys[pygame.K_SPACE] and countdown == 0 and money >= bet:
        pos_x_choices = [i for i in range(331, 470)]
        pos_x_choices.remove(400)
        pos_x_choices.remove(365)
        pos_x_choices.remove(435)

        random_pos_x = choice(pos_x_choices)
        random_pos_y = randint(60, 130)
        random_pos = (random_pos_x, random_pos_y)
        apples.append(Apple(space, random_pos, k, bet))
        money -= bet

        for j in range(9):
            a = space.add_collision_handler(apples[-1].shape.collision_type,j+1)
            handlers[j].append(a)

        k += 1
        countdown = 20

    if (keys[pygame.K_UP] or keys[pygame.K_DOWN]) and bet_countdown == 0:
        if keys[pygame.K_UP] and bet+0.25 <= money:
            bet += 0.25
        if keys[pygame.K_DOWN] and bet > 0.25:
            bet -= 0.25
        bet_countdown = 10

    for m, lista in enumerate(handlers):
        for i, handler in enumerate(lista):
            handler.begin = apples[i].collision[m]

    if countdown > 0:
        countdown -= 1
    else:
        keys = pygame.key.get_pressed()
    if bet_countdown > 0:
        bet_countdown -= 1

    money_text = RenderText(f'{money}$', 30, (255,0,0))
    win.blit(money_text, (650, 25))

    bet_text = RenderText(f'bet = {bet}$', 30, (255,0,0))
    win.blit(bet_text, (50, 25))

    draw_apples(apples)
    draw_static_ball(balls)
    draw_multiplier(multipliers)

    for h, title in enumerate(multipliers_title):
        win.blit(title, (multiplier_rect[h]))

    space.step(1/50)
    pygame.display.update()
    clock.tick(120)

pygame.quit()
sys.exit()