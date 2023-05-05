from dino_runner.utils.constants import RELOGIO, RELOGIO_TYPE
from dino_runner.components.powerups.power_up import PowerUp


class Relogio(PowerUp):
    def __init__(self):
        super().__init__(RELOGIO, RELOGIO_TYPE)