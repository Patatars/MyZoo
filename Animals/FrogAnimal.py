from BaseAnimal import *


class FrogAnimal(BaseAnimal):
    def __init__(self, name, age):
        super().__init__(name, age, "forest", 1, ["fly", "mosqute"], False, "qwa", 1)
