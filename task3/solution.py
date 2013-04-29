class Person:
    def __init__(self, name, birth_year, gender, mother=None, father=None):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.parents = [parent for parent in [mother, father] if parent]
        self.kids = []
        if mother:
            mother.kids.append(self)
        if father:
            father.kids.append(self)

    def children(self, gender=None):
        if gender:
            return list(filter(lambda kid: kid.gender == gender, self.kids))
        else:
            return self.kids

    def siblings(self, gender=None):
        children = set([kid for parent in self.parents
                        for kid in parent.kids])
        children -= {self}

        if gender:
            return [kid for kid in children if kid.gender == gender]
        else:
            return children

    def get_brothers_and_sisters(self):
        return self.siblings()

    def get_brothers(self):
        return self.siblings('M')

    def get_sisters(self):
        return self.siblings('F')

    def is_direct_successor(self, person):
        return person in self.kids
