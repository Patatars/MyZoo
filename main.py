from Animal import Animal

if __name__ == '__main__':
    pete = Animal("Петя", 5, "Слон", foodTypes=["Мясо", "Трава"], foodVolume=5)
    simba = Animal("Симба", 5, "Пингвин", biome="Тундра", needArea=10, foodTypes=["Рыба", "Мясо"], sound="Хрю",
                   foodVolume=1)
    matilde = Animal("Матильяда", 10, "Тигр", predator=True, foodVolume=2, foodTypes=["Мясо"])

    pete.doSound()
