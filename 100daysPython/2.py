class Duck:
    def quack(self):
        return "Quack!"

class Dog:
    def quack(self):  # Dog can "quack" too
        return "Woof! (pretending to quack)"

def make_it_quack(animal):
    return animal.quack()  # Doesn't check type, just calls quack()

# Both work because they have quack() method
print(make_it_quack(Duck()))  # "Quack!"
print(make_it_quack(Dog()))   # "Woof! (pretending to quack)"