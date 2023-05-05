from dino_runner.utils.constants import TORPEDO
from dino_runner.components.obstacles.obstacle import Obstacle

from random import randint
class Torpedo(Obstacle):
    def __init__(self, game):
    
        super().__init__(TORPEDO, 0)
        self.rect.y = randint(300,340)
        self.index = 0
        if game.player.fly == True:
           self.rect.y = randint(100, 200)
        

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index//5], self.rect)
        self.index += 1