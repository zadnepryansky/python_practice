class GameCharacter:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def speak(self):
        print('Hi my name is ' + self.name)


class Villain(GameCharacter):
    def __init__(self, name, health, level):
        GameCharacter.__init__(self,name, health, level)

    def speak(self):
        print('Hi my name is ' + self.name + ' and I will kill you')

    def kill(self, other):
        other.health = 0
        print('Bang-bang, now you\'re dead')


dima = GameCharacter('Dima', 100, 99)
karina = Villain('Karina', 100, 80 )

dima.speak()
karina.speak()
print(dima.health)
karina.kill(dima)
print(dima.health)
