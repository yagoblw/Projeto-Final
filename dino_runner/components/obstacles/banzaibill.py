from dino_runner.utils.constants import BANZAIBILL
from dino_runner.components.obstacles.obstacle import Obstacle

class BanzaiBill(Obstacle):
    def __init__(self):
        super().__init__(BANZAIBILL, 0)
        self.rect.y = 300
    
    def draw(self, screen):
        screen.blit(self.image[0], self.rect)
        
        