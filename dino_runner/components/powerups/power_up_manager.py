import random
from time import time
import pygame

from dino_runner.components.powerups.pena import Pena
from dino_runner.components.powerups.shield import Shield 
from dino_runner.components.powerups.hammer import Hammer
from dino_runner.components.powerups.time import Relogio
from dino_runner.components.powerups.coração import Heart
from dino_runner.utils.constants import HAMMER_TYPE, SHIELD_TYPE, RELOGIO_TYPE, PENA_TYPE, HEART_TYPE, SOUNDS

POWER_UPS = [Heart(),Pena(),Shield(),Hammer(),Relogio()]

class PowerUpManager:
    def __init__(self):
        self.power_ups = list()
        self.when_appears = 0
       
    
    def generate_power_up(self, score, limite):
        if len(self.power_ups) == 0 and self.when_appears == score:
            self.when_appears += random.randint(200, 300)
            self.power_ups.append(POWER_UPS[random.randint(0, limite)])

    def update(self, score, game_speed, player, game):
            if not player.fly:
               if game_speed < 30:
                    limite  = 3
               else:
                    limite = len(POWER_UPS) - 1
               self.generate_power_up(score, limite)
               for power_up in self.power_ups:
                    power_up.update(game_speed, self.power_ups)
                    if player.dino_rect.colliderect(power_up.rect):
                        SOUNDS["Coin"].play()
                
                        power_up.start_time = pygame.time.get_ticks()
                        
                       
                        if power_up.type == HEART_TYPE or power_up.type == PENA_TYPE:
                            if power_up.type != HEART_TYPE:
                                  player.type = power_up.type
                            player.duraveis[power_up.type].append(power_up.image)
                            if power_up.type == HEART_TYPE and len(player.duraveis[PENA_TYPE]) > 0:
                                 player.type = PENA_TYPE
                        else: 
                            player.type = power_up.type
                            player.has_power_up = True   
                            player.duraveis[PENA_TYPE].clear() 
                            if player.type == SHIELD_TYPE:
                                player.power_up_time = power_up.start_time + (power_up.duration * 700)
                                player.shield = True

                            elif player.type == HAMMER_TYPE:
                                    player.power_up_time = power_up.start_time + (power_up.duration * 700)
                                    player.hammer = True

                            elif player.type == RELOGIO_TYPE:
                                    game.game_speed -= 10

                        print(player.type)
                        self.power_ups.remove(power_up)
                    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups.clear()
        self.when_appears = random.randint(200, 300)
