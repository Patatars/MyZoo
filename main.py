from Animal import Animal

if __name__ == '__main__':
    pete = Animal("Слон", "Тропики", 10, ["Рыба"], False, "Ауф")
    pete.name = "Петя"
    pete.foodVolume = 5
    pete.age = 5
    simba = Animal("Пингвин", "Тундра", 10, ["Рыба", "Мясо"], False, "Хрю")
    simba.name = "Симба"
    simba.age = 1
    matilde = Animal("Тигр", "Пустыня", 10, ["Рыба", "Мясо"], True, "Рррррр")
    matilde.name = "Матильда"
    matilde.foodVolume = 0.3
    matilde.age = 20

    pete.doSound()

