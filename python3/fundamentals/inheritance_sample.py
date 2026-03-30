class Animal:
    def __init__(self):
        self.is_live = True

    def eat(self):
        print("eat")


class Cat(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.has_scales = True

    def swime(self):
        print("swime")


cat = Cat()
cat.eat()
cat.walk()
print(cat.is_live)
fish = Fish()
fish.swime()

print(isinstance(cat, Animal))
print(isinstance(cat, object))
print(isinstance(fish, Cat))

print(issubclass(Cat, Animal))
print(issubclass(Cat, object))
print(issubclass(Fish, Cat))
