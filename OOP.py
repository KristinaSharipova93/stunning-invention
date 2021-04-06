class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

        self.key = (name)

    def __repr__(self):
        return "Person('%s',%s,%s)" % (self.name, self.age, self.height)

Kristina = Person ( "Кристина", 27, 165 )
Masha = Person ( "Маша", 30, 170 )
Dasha = Person ( "Даша", 28, 165 )
people = {
    Kristina.key: Kristina,
    Masha.key: Masha,
    Dasha.key: Dasha,
}
print ( people )
print ( people[Masha.key] )
