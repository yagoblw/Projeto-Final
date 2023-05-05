import pygame
from winsound import PlaySound
from pygame import mixer
from random import randint
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, CLOUD, RESET, MUSIC,START, BG2, BG_MENU_DEATH, START_MUSIC, FUNDO_START
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.text_utils import draw_message_component
from dino_runner.components.powerups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        mixer.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.death_count = 0
        self.x_pos_bg = 0
        self.y_pos_bg = -600
        self.x_pos_cloud = 0
        self.y_pos_cloud = 20
        self.best_score = 0 
        self.index = 0
        self.index_start = 0
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

        self.music(START_MUSIC, volume= 0.9)

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()        

    def run(self):
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.game_speed = 20
        self.score = 0
        
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player, self)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 0.5
        
        if self.score >= self.best_score:
            self.best_score = self.score
               
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) 
        self.draw_background()
        self.draw_cloud()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_power_up_time()
        self.draw_duraveis()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG2, (0 , -15))
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.x_pos_bg = 0
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        self.x_pos_bg -= self.game_speed - 10

    def draw_cloud(self):
        image = CLOUD[self.index]
        image_width = image.get_width()
        if self.x_pos_cloud <= - SCREEN_WIDTH:
            self.x_pos_cloud = 1000
            self.y_pos_cloud = randint(20,150)
            self.index = randint(0,1)
        self.screen.blit(image, (self.x_pos_cloud, self.y_pos_cloud))
        self.screen.blit(image, (image_width + self.x_pos_cloud, self.y_pos_cloud - 10))
        self.screen.blit(CLOUD[0], (image_width + self.x_pos_cloud, self.y_pos_cloud + 20))
        self.x_pos_cloud -= self.game_speed - 5

    def draw_score(self):
            draw_message_component(
                f"Score: {self.score}",
                self.screen,
                font_color=(0,0,0),
                pos_x_center=1000,
                pos_y_center=80
            )

            draw_message_component(
                f"Maior pontuação: {self.best_score}",
                self.screen,
                pos_y_center= 60,
                pos_x_center=925,
                font_color= (0, 0, 0)
            )
          
    def draw_power_up_time(self):
        if self.player.has_power_up: 
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                draw_message_component(
                    f"{self.player.type.capitalize()} enabled for {time_to_show} segundos",
                    self.screen,
                    font_size = 18,
                    pos_x_center = 500,
                    pos_y_center = 100
                )
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def draw_duraveis(self):

        coração = len(self.player.duraveis["heart"])
        if len(self.player.duraveis["heart"]) > 0:
            draw_message_component(
                f"Vidas: {coração}",
                self.screen,
                font_size = 18,
                pos_x_center = 55,
                pos_y_center = 20,
            ) 

        if len(self.player.duraveis["Pena"]) > 0:
            X = SCREEN_WIDTH // 2 - 20
            image = self.player.duraveis["Pena"][0]
            heigth = image.get_height()
            self.screen.blit(image,(X, 0))
            draw_message_component(
                f"PRESS W/Q",
                self.screen,
                font_size = 15,
                pos_x_center = X,
                pos_y_center = heigth + 8,
            ) 

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.music(MUSIC, 0.2)
                self.run()  

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_heigth = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2


        if self.death_count == 0:
           draw_message_component("Pressione qualquer tecla", self.screen, font_size= 40, pos_y_center= half_screen_heigth + 50)
           if self.index_start > 9:
               self.index_start = 0 
           self.screen.blit(START[int(self.index_start) // 5], (0, 0))
           self.index_start += 0.1
          
        else:
            draw_message_component("Pressione qualquer tecla", self.screen, pos_y_center = half_screen_heigth + 155)
            self.draw_score()
            self.screen.blit(BG_MENU_DEATH, (0,0))
            self.screen.blit(RESET, (half_screen_width - 30, half_screen_heigth + 200 ))


            draw_message_component(
                f"Sua pontuação: {self.score}",
                self.screen,
                pos_y_center= half_screen_heigth - 60,
                font_color= (255,255,255)
            )

            draw_message_component(
                f"Maior pontuação: {self.best_score}",
                self.screen,
                pos_y_center= half_screen_heigth - 90,
                font_color= (255,255,255)
            )

            draw_message_component(
                f"Mortes: {self.death_count}",
                self.screen,
                font_color=(255,255,255),
                pos_x_center=550,
                pos_y_center=270
                        )   


        pygame.display.flip()
        self.handle_events_on_menu()    

    def music(self, music, volume):
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(volume) 
