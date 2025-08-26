class Father:
    def skill(self):
        print("I am father parent class")

class Mother:
    def skill(self):
        print("I am in Mother parent class")

class Son(Father, Mother):
    def skill(self):
        Father.skill(self)
        Mother.skill(self)
        print(" I am in child sub class")

s = Son()
s.skill()