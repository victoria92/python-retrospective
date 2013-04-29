class Person:
    def __init__(self, name, birth_year, gender, mother=None, father=None):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.mother = mother
        self.father = father
        self.kids = []
        if mother:
            mother.kids.append(self)
        if father:
            father.kids.append(self)

    def female(self):
        return self.gender == 'F'

    def male(self):
        return self.gender == 'M'

    def children(self, gender=None):
        if gender:
            return [kid for kid in self.kids if kid.gender == gender]
        else:
            return self.kids

    def get_brothers_and_sisters(self):
        mother_kids = self.mother.kids if self.mother else []
        father_kids = self.father.kids if self.father else []
        return set(mother_kids + father_kids) - {self}

    def get_brothers(self):
        return [kid for kid in self.get_brothers_and_sisters() if kid.male()]

    def get_sisters(self):
        return [kid for kid in self.get_brothers_and_sisters() if kid.female()]

    def is_direct_successor(self, person):
        return person in self.kids
