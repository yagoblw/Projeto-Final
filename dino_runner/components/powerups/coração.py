from dino_runner.utils.constants import HEART, HEART_TYPE
from dino_runner.components.powerups.power_up import PowerUp

class Heart(PowerUp):
    def __init__(self):
        super().__init__(HEART, HEART_TYPE)     