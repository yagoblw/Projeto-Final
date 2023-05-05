import pygame
import random
from pygame import mixer
from dino_runner.components.obstacles.dragao import Dragao
from dino_runner.components.obstacles.torpedo import Torpedo
from dino_runner.components.obstacles.tartaruga import Tartaruga
from dino_runner.components.obstacles.banzaibill import BanzaiBill
from dino_runner.components.obstacles.cogumelovoador import CogumeloVoador
from dino_runner.utils.constants import HAMMER_TYPE, SHIELD_TYPE, DEATH_SOND, HEART_TYPE, PENA_TYPE, DEFAULT_TYPE, SOUNDS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        obstacles = [Torpedo(game), CogumeloVoador(game),Tartaruga(), Dragao(), BanzaiBill()]

        if len(self.obstacles) == 0:  
            if game.player.fly:
                self.obstacles.append(obstacles[random.randint(0, 1)])
            else: 
                self.obstacles.append(obstacles[random.randint(0, 4)])

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                SOUNDS["Colisão"].play()
                if not game.player.has_power_up and len(game.player.duraveis[HEART_TYPE]) == 0 and  len(game.player.duraveis[PENA_TYPE]) == 0:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    self.musica_de_morte()
                    break
                else: 
                        if game.player.type == HAMMER_TYPE:   
                           self.obstacles.remove(obstacle)
                                
                        elif game.player.type == SHIELD_TYPE:
                            self.obstacles.remove(obstacle)  

                        elif game.player.type == PENA_TYPE:
                            self.obstacles.remove(obstacle) 
                            game.player.fly = False
                            game.player.type = DEFAULT_TYPE
                            game.player.jump()
                            game.player.has_power_up = False
                            game.player.duraveis[PENA_TYPE].clear()

                        elif len(game.player.duraveis[HEART_TYPE]) > 0:
                            self.obstacles.remove(obstacle)
                            game.player.duraveis[HEART_TYPE].pop()

                       
                       
    def reset_obstacles(self):
        self.obstacles = []     

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)        

    def musica_de_morte(self):
        pygame.mixer.music.load(DEATH_SOND)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.5)