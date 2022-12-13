from BaseAnimal import *


class BirdAnimal(BaseAnimal):
    def __init__(self, name, age):
        super().__init__(name, age, "air", 1, ["worm", "berry"], False, "kurlik kurlik", 1)
