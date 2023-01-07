from Animals.BaseAnimal import BaseAnimal


class BearAnimal(BaseAnimal):
    def __init__(self, name, age):
        super().__init__(name, age, "forest", 5, ["fish", "berry", "meat"], True, "rrrrrr", 5)
