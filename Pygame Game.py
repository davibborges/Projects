import sys, pygame, time
pygame.init()
from random import randint

'''Definições importantes'''
#Biblioteca de cores
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
dark_blue = (8, 3, 36)
#Resolução da tela
size = width, height = 1366, 768
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Imperium Invaders")
inicio_x = 333
inicio_y = 80

def tela_vitoria():
    while True:
        screen.fill(black)

        title = font.render("YOU SAVED THE GALAXY!", True, white)
        exit = pygame.font.Font("Orbitron.ttf", 25).render("Press ESC to quit", True, white)

        screen.blit(title, (width//2 - title.get_width()//2, 300))
        screen.blit(exit, (width//2 - exit.get_width()//2, 380))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

#Fonte
font = pygame.font.Font("Orbitron.ttf", 15)
font.set_bold(False)

'''Jogador'''
#Tamanho do Jogador
#Distância do Jogador
player_x = width // 2
player_y = 653

#Velocidade
speed = 10

#Texto
font = pygame.font.Font('Orbitron.ttf', 45)
font.set_bold(False)
points = 0
player_life = 3

#Música e Som
pygame.mixer.music.set_volume(0.3)
background_music = pygame.mixer.music.load("psychronic.mp3")
pygame.mixer.music.play(-1)
laser_vfx = pygame.mixer.Sound("laser.wav")
laser_vfx.set_volume(0.60)
sweep_vfx = pygame.mixer.Sound("sweep.wav")
sweep_vfx.set_volume(0.60)

#Inimigos
enemies = []
for linha in range(2):
    for coluna in range(10):
        tiefighter_x = inicio_x + coluna * 100
        tiefighter_y = inicio_y + linha * 90

        enemies.append([tiefighter_x, tiefighter_y])

#Spaceship(BOSS)
boss_active = False
boss_warning_played = False
spaceship_x = width // 2
spaceship_y = 220
spaceship_life = 24


#Variáveis de movimento
enemy_speed = 5
enemy_direction = 1

spaceship_speed = 3
spaceship_direction = 1

'''Imagens Importantes'''
#Imagem do Jogador:
sprite = pygame.image.load("xwing128px.png")
#sprite = pygame.transform.scale(sprite, (256, 256))
#Imagem dos direçaos
tiefighter = pygame.image.load("tiefighter128px.png")
#tiefighter = pygame.transform.scale(tiefighter, (182, 182))
spaceship = pygame.image.load("spaceship.png")
#Laser
lasers = []
tiefighter_lasers = []
spaceship_lasers = []
#Pontuação
points = 0

#Fundo Estrelado
stars = []

for i in range(120):
    x = randint(0, width)
    y = randint(0, height)
    star_speed = randint(1, 3)

    stars.append([x, y, star_speed])

#FPS
clock = pygame.time.Clock()
while True:
    #FPS MAXIMO
    clock.tick(60)
    #Encerramento do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    #Laser do Jogador    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                lasers.append([player_x, player_y - 40])
                laser_vfx.play() 
    for laser in lasers:
        laser[1] -= 10

    #Laser do Tiefighter
    count = randint(1, 20)
    if count == 20:
        if enemies:
            enemy = enemies[randint(0, len(enemies)-1)]
            tiefighter_lasers.append([enemy[0], enemy[1] + 40])

    for laser in tiefighter_lasers:
        laser[1] += 7

        if len(enemies) == 0:
            break

    #Laser do Spaceship
    if count == 5:
        spaceship_lasers.append([spaceship_x - 6, spaceship_y + 80])
    
    for laser in spaceship_lasers:
        laser[1] += 12

    #Contagem de pontos
    points_message = f'Points: {points}'
    formated_points = font.render(points_message, True, white)
    life_message = f'Life: {player_life}'
    formated_life = font.render(life_message, True, white)

    #Movimentação
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        player_x -= speed
    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        player_x += speed
    if teclas[pygame.K_w] or teclas[pygame.K_UP]:
        player_y -= speed
    if teclas[pygame.K_s] or teclas [pygame.K_DOWN]:
        player_y += speed

    #Ultrapassamento da tela
    if player_x > width - 64:
        player_x = width - 64

    if player_x < 64:
        player_x = 64

    if player_y < 64:
        player_y = 64

    if player_y > height - 64:
        player_y = height - 64

    '''Movimento dos inimigos'''
    #Tiefighter
    for enemy in enemies:
        enemy[0] += enemy_speed * enemy_direction

    #Spaceship
    spaceship_x += spaceship_speed * spaceship_direction

    '''Mudança de direção após atingir borda'''
    
    #Tiefighter
    for direction in enemies:

        if direction[0] >= width - 70:
            enemy_direction = -1

            for i in enemies:
                i[1] += 30

            break

        if direction[0] <= 70:
            enemy_direction = 1

            for j in enemies:
                j[1] += 30

            break

    #Spaceship
    if spaceship_x >= width - 90:
        spaceship_direction = -1

    if spaceship_x <= 90:
        spaceship_direction = 1
         
    #Fundo da tela
    screen.fill(dark_blue)

    #Desenho das estrelas 
    for star in stars:

        star[1] += star[2]

        if star[1] > height:
            star[1] = 0
            star[0] = randint(0, width)

        pygame.draw.circle(
            screen,
            white,
            (star[0], star[1]),
            2
        )

    #Desenho do Tiefighter
    for direçao in enemies:
        tiefighter_rect = tiefighter.get_rect(center=(direçao[0], direçao[1]))
        screen.blit(tiefighter, tiefighter_rect)
    
    #Desenho do Boss
    if boss_active == True:
        spaceship_rect = spaceship.get_rect(center=(spaceship_x, spaceship_y))
        screen.blit(spaceship, spaceship_rect)

        for laser in spaceship_lasers:
            spaceship_laser_rect = pygame.draw.rect(screen, red, (laser[0], laser[1], 10, 18))

            if spaceship_laser_rect.colliderect(sprite_rect):
                player_life -= 1
                spaceship_lasers.remove(laser)


    #Desenho do jogador
    sprite_rect = sprite.get_rect(center=(player_x, player_y))
    screen.blit(sprite, sprite_rect)

    #Desenho dos lasers
    for laser in tiefighter_lasers:
        tf_laser_rect = pygame.draw.rect(screen, red, (laser[0], laser[1], 4, 18))

        if tf_laser_rect.colliderect(sprite_rect):
            player_life -= 1
            tiefighter_lasers.remove(laser)
        if boss_active == True:
            tiefighter_lasers.remove(laser)

    for laser in lasers:
        laser_rect = pygame.draw.rect(screen, green,(laser[0], laser[1], 4, 18))

        for enemy in enemies[:]:
            tf_rect = tiefighter.get_rect(center=(enemy[0], enemy[1]))

            if laser_rect.colliderect(tf_rect):
                lasers.remove(laser)
                enemies.remove(enemy)

                points += 100

                break

        if boss_active == True:
            if laser_rect.colliderect(spaceship_rect):
                lasers.remove(laser)
                spaceship_life -= 2
                points += 350
                
                if spaceship_life == 0:
                    tela_vitoria()

        
    if not enemies:
        boss_active = True

        if not boss_warning_played:
            sweep_vfx.play()
            boss_warning_played = True
                
            
    screen.blit(formated_points, (30, 35))
    screen.blit(formated_life, (30, 75))
    if player_life <= 0:
        player_x = width // 2
        player_y = 653

        player_life = 3
        points = 0

        boss_active = False
        boss_warning_played = False

        spaceship_x = width // 2
        spaceship_life = 24

        lasers.clear()
        tiefighter_lasers.clear()
        spaceship_lasers.clear()

        enemies.clear()

        for linha in range(2):
            for coluna in range(10):
                tiefighter_x = inicio_x + coluna * 100
                tiefighter_y = inicio_y + linha * 90

                enemies.append([tiefighter_x, tiefighter_y])
    
    pygame.display.flip()

pygame.quit()
sys.exit
