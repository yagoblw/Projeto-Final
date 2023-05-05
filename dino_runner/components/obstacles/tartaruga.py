from dino_runner.utils.constants import TARTARUGA
from dino_runner.components.obstacles.obstacle import Obstacle

class Tartaruga(Obstacle):
    def __init__(self):
        super().__init__(TARTARUGA, 0)
        self.rect.y = 396
        self.index = 0
        
    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.image[self.index//5], self.rect)
        self.index += 1