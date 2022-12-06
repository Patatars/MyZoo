from BaseAnimal import *
from BearAnimal import BearAnimal
from CatAnimal import CatAnimal
from FrogAnimal import FrogAnimal
from Valier import Valier

if __name__ == '__main__':
    v = Valier("home")
    print(v.addAnimal(CatAnimal("qqq", 7)))
    print(v.addAnimal(FrogAnimal("wqqq", 7)))
    v.feedAnimals("meat", 20)

