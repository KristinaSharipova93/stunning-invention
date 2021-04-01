from pprint import pprint
class Person:
    def __init__(self, name , age, height):
        self.name, self.age, self.height = name, age, height,
        self.key = (name , age)
    def __repr__(self):
        return "Person('%s',%s,%s)" % (self.name, self.age, self.height)

Kristina = Person("Кристина", 27, 165)
Masha = Person("Маша", 30, 170)
Dasha = Person("Даша", 28, 165)
people = {
Kristina.key: Kristina,
Masha.key: Masha,
Dasha.key: Dasha,
}
pprint(people)
pprint(people[Masha.key])
