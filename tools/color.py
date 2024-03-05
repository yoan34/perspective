from enum import Enum


class Color(Enum):
    WHITE = (180, 180, 180)
    RED = (196, 30, 58)
    BLUE = (0, 81, 186)
    ORANGE = (255, 88, 0)
    YELLOW = (255, 213, 0)
    GREEN = (0, 155, 72)
    
    @property
    def rgb(self):
        return self.value