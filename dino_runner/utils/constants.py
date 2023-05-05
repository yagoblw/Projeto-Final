import pygame
import os

pygame.mixer.init()

def iterarSpritSheet(LISTA, OBJETO, NUMERO_DE_FRAMES, X, Y, scale_x=1, scale_y=1):
    for i in range(NUMERO_DE_FRAMES):
            img  = 0
            img = OBJETO.subsurface((i*X,0), (X, Y))
            img = pygame.transform.scale(img,( X*scale_x, Y*scale_y))
            LISTA.append(img)

TITLE = "Mario Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN_CENTER_WIDTH = SCREEN_WIDTH//2
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
BG_MENU_DEATH = pygame.transform.scale( pygame.image.load(os.path.join(IMG_DIR, "cenario/menu_game_over.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))
BG = pygame.image.load(os.path.join(IMG_DIR, 'cenario/Cenário5.png'))
BG2 = pygame.image.load(os.path.join(IMG_DIR, 'cenario/cenario11.png'))
FONT = os.path.join( 'dino_runner/assets/Other/Retro Gaming.ttf')

HEIGH = 97
WIDTH = 100

ICON = pygame.image.load(os.path.join(IMG_DIR, "Mario/marioIcon.png"))
GAMEOVER = pygame.image.load(os.path.join(IMG_DIR, "Other/GameOver.png"))
RESET = pygame.image.load(os.path.join(IMG_DIR, "Other/Reset.png"))
DEATH = pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioSprit.png")).subsurface((500, 388),(100, 97))

START = [pygame.image.load(os.path.join(IMG_DIR, "cenario/StartMario1.png")),
         pygame.image.load(os.path.join(IMG_DIR, "cenario/StartMario2.png")),
         ]

FUNDO_START  = pygame.image.load(os.path.join(IMG_DIR, "cenario/FUNDO.png"))


FLY_RUN =  pygame.image.load(os.path.join(IMG_DIR, "Mario/mariofly_run.png"))
FLY_JUMP = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario/mariofly.png")).subsurface((274, 193), (92, 97)), (100, 97))
DUCK = pygame.image.load(os.path.join(IMG_DIR, "Mario/maro_duck.png"))
MARIO_FLY = pygame.image.load(os.path.join(IMG_DIR, "Mario/mario_fly.png"))
MARIO_RUN = pygame.image.load(os.path.join(IMG_DIR, "Mario/mario_run.png"))
MARIO_RUN_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "power_ups/mecha_consertado.png"))
JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioSprit.png")).subsurface((0, 194),(100, 97))
JUMPING_SHIELD = pygame.transform.scale2x(pygame.image.load(os.path.join(IMG_DIR, "power_ups/mecajump.png")))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioSprit.png")).subsurface((300, 388),(100, 97))
DUCKING_SHIELD =[ pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Mario/marioKart.png")), (96 * 0.7, 100 * 0.7))]
MARIO_HAMMER  = pygame.image.load(os.path.join(IMG_DIR, "power_ups/mario_hammer_consertado2.png"))
TARTARUGAM =  pygame.image.load(os.path.join(IMG_DIR, "obstaculo/tartarugaM.png"))
TOPEDOS =  pygame.image.load(os.path.join(IMG_DIR, "obstaculo/torpedoS.png"))
DRAGAO1 =  pygame.image.load(os.path.join(IMG_DIR, "obstaculo/dragao.png"))
COGUMELO_VOADOR_IMG =  pygame.image.load(os.path.join(IMG_DIR, 'obstaculo/cogumeloVoador2.png'))
BANZAIBILL = [pygame.image.load(os.path.join(IMG_DIR, 'obstaculo/BanzaiBill.png'))]

RUNNING_SHIELD = list()
iterarSpritSheet(RUNNING_SHIELD, MARIO_RUN_SHIELD,3 ,100, 97)

RUNNING_HAMMER = list()
iterarSpritSheet(RUNNING_HAMMER, MARIO_HAMMER, 3, 100, 97)

RUNNING = list()
iterarSpritSheet(RUNNING, MARIO_RUN, 2, 100, 97)

VOANDO = list()
iterarSpritSheet(VOANDO, MARIO_FLY, 2, 92, 97)

FLY_RUNING = list()
iterarSpritSheet(FLY_RUNING, FLY_RUN, 5, 91, 97)

DUCKING = list()
iterarSpritSheet(DUCKING, DUCK, 2, 100, 97)

TARTARUGA = list()
iterarSpritSheet(TARTARUGA, TARTARUGAM, 2, 60, 60)

TORPEDO = list()
iterarSpritSheet(TORPEDO,TOPEDOS, 2, 96, 48)

DRAGAO = list()
iterarSpritSheet(DRAGAO, DRAGAO1, 2, 50, 80 )

COGUMELO_VOADOR = list() 
iterarSpritSheet(COGUMELO_VOADOR, COGUMELO_VOADOR_IMG, 4, 80, 67 )                       

CLOUD =[pygame.image.load(os.path.join(IMG_DIR, 'cenario/nuvem.png')),
        pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'cenario/nuvem2.png')),(90 * 1.5, 36*1.5)),]

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'powerUpIcon/escudo.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'powerUpIcon/HammerM.png'))
RELOGIO = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'powerUpIcon/relogio.png')),(418 * 0.1 , 597 * 0.1))
HEART = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'powerUpIcon/life.png')),(16 * 1.9, 16*1.9))
PENA = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, 'powerUpIcon/pena.png')),(40, 40))

MUSIC = "dino_runner/assets/Sounds/SuperMarioTheme.mp3"
DEATH_SOND = "dino_runner/assets/Sounds/GameOver.mp3"
START_MUSIC = "dino_runner/assets/Sounds/Start.mp3"
SOUNDS ={
    "Colisão": pygame.mixer.Sound("dino_runner/assets/Sounds/colisao.mp3"),
    "Coin": pygame.mixer.Sound("dino_runner/assets/Sounds/coin.wav"),
    "Jump":  pygame.mixer.Sound("dino_runner/assets/Sounds/jump.wav"),
} 

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "martelo"
RELOGIO_TYPE = "relógio"
PENA_TYPE = "Pena"
HEART_TYPE = "heart"

