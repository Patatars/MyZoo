from Animals.CatAnimal import CatAnimal
from Valier import Valier

if __name__ == '__main__':
    cat = CatAnimal("qqq", 12)
    v = Valier("home")
    v.addAnimal(cat)
    v.addFood("meat", 2)
    v.addFood("fish", 78)
    v.feedAnimals()
    print(v.getHungryAnimals())
    print(v.foodRemaining)


