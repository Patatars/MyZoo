from BaseAnimal import *


class CatAnimal(BaseAnimal):
    def __init__(self, name, age):
        super().__init__(name, age, "home", 2, ["fish", "meat"], False, "meow", 3)
