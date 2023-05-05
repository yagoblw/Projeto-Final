from dino_runner.utils.constants import PENA, PENA_TYPE
from dino_runner.components.powerups.power_up import PowerUp

class Pena(PowerUp):
    def __init__(self):
        super().__init__(PENA, PENA_TYPE)

    