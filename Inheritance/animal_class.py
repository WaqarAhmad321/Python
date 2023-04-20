class Animal():
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def makesound(self):
        print(f"{self.sound}")


class Cat(Animal):
    def __init__(self, name, sound):
        Animal.__init__(self, name, sound)

    def makesound(self):
        print(f"{self.sound}")


cat = Cat("cat", "Meow")
cat.makesound()
animal = Animal("Dog", "Bark")
