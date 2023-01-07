import unittest

from Animals import *
from Animals.BearAnimal import BearAnimal
from Animals.CatAnimal import CatAnimal
from Animals.FrogAnimal import FrogAnimal
from Valier import Valier
from Zoo import Zoo


class test(unittest.TestCase):
    def setUp(self):
        self._animal = BearAnimal("Медведь1", 228)
        self._animal2 = BearAnimal("Медведь2", 228)
        self._animalAnotherBiome = CatAnimal('Кот1', 78)
        self._peaceAnimal = FrogAnimal("Лягушка1", 228)
        self._valier = Valier(self._animal.biome, area=9999)
        self._smallValiers = Valier(self._animal.biome, area=1)
        self._zoo = Zoo()

    def testEatInvalidFood(self):
        expected = False
        actual = self._animal.eat({'bebebe': 78})
        self.assertEqual(expected, actual)

    def testAnimalIsFeeded(self):
        self._animal.eat({self._animal.foodTypes[0]: 999999})
        expected = False
        actual = self._animal.eat({self._animal.foodTypes[0]: 999999})
        self.assertEqual(expected, actual)

    def testOkFood(self):
        expected = True
        actual = self._animal.eat({self._animal.foodTypes[0]: 999999})
        self.assertEqual(expected, actual)

    def testAddAddedAnimal(self):
        self._valier.addAnimal(self._animal)
        expected = False
        actual = self._valier.addAnimal(self._animal)
        self.assertEqual(expected, actual)

    def testAddIncorrectBiomeAnimal(self):
        expected = False
        actual = self._valier.addAnimal(self._animalAnotherBiome)
        self.assertEqual(expected, actual)

    def testAddAnimalWithExtraSize(self):
        expected = False
        actual = self._smallValiers.addAnimal(self._animal)
        self.assertEqual(expected, actual)

    def testAddPredatorToNotPredators(self):
        expected = False
        self._valier.addAnimal(self._peaceAnimal)
        actual = self._valier.addAnimal(self._animal)
        self.assertEqual(expected, actual)

    def testAddNotPredatorToPredators(self):
        expected = False
        self._valier.addAnimal(self._animal)
        actual = self._valier.addAnimal(self._peaceAnimal)
        self.assertEqual(expected, actual)

    def testAddCorrectAnimal(self):
        expected = True
        self._valier.addAnimal(self._animal)
        actual = self._valier.addAnimal(self._animal2)
        self.assertEqual(expected, actual)

    def testRemoveInvalidAnimal(self):
        expected = False
        actual = self._valier.removeAnimal(self._animal)
        self.assertEqual(expected, actual)

    def testRemoveValidAnimal(self):
        expected = True
        self._valier.addAnimal(self._animal)
        actual = self._valier.removeAnimal(self._animal)
        self.assertEqual(expected, actual)

    def testGetHungryAnimals(self):
        expected = [self._animal]
        self._valier.addAnimal(self._animal)
        actual = self._valier.getHungryAnimals()
        self.assertEqual(expected, actual)

    def testGetFoodNeed(self):
        self._valier.addAnimal(self._animal)
        expected = {self._animal.foodTypes[0]: self._animal.needFood}
        actual = self._valier.getFoodNeed()
        self.assertEqual(expected, actual)

    def testRemoveInvalidValier(self):
        expected = False
        actual = self._zoo.removeValier(self._valier)
        self.assertEqual(expected, actual)

    def testRemoveValidValier(self):
        expected = True
        self._zoo.addValier(self._valier)
        actual = self._zoo.removeValier(self._valier)
        self.assertEqual(expected, actual)
