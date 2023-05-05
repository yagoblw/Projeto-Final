from dino_runner.utils.constants import COGUMELO_VOADOR
from dino_runner.components.obstacles.obstacle import Obstacle

from random import randint
class CogumeloVoador(Obstacle):
    def __init__(self, game):
        super().__init__(COGUMELO_VOADOR, 0)
        self.rect.y = randint(290,320)
        self.index = 0
        if game.player.fly == True:
           self.rect.y = randint(100, 200)
    
        

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index//5], self.rect)
        self.index += 1