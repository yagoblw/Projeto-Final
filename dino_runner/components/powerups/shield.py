from dino_runner.utils.constants import SHIELD, SHIELD_TYPE
from dino_runner.components.powerups.power_up import PowerUp


class Shield(PowerUp):
    def __init__(self):
        super().__init__(SHIELD,SHIELD_TYPE )