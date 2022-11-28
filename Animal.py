class Animal:
    def __init__(self, name, age, species, biome="default", needArea=1, foodTypes=None, predator=False, sound="",
                 foodVolume=1):
        if foodTypes is None:
            foodTypes = []
        self.__species = species
        self.__biome = biome
        self.__needArea = needArea
        self.__foodTypes = foodTypes
        self.__predator = predator
        self.__isFeeded = False
        self.__foodEated = 0
        self.__sound = sound
        self.__foodVolume = foodVolume
        self.__name = name
        self.__age = age

    @property
    def Feeded(self):
        return self.__isFeeded

    def doSound(self):
        print(self.__sound)

    def eat(self, foodType):
        if foodType not in self.__foodTypes:
            return
        if self.__isFeeded:
            return
        if self.__foodEated >= self.__foodVolume:
            self.__isFeeded = True
            return
        if foodType in self.__foodTypes:
            self.__foodEated += 1
            if self.__foodEated >= self.__foodVolume:
                self.__isFeeded = True
                self.__foodEated = 0

    def play(self):
        print("Я играю")
