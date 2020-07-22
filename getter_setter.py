# define a class with getter, setter methods in it
# example of patient
# fields as id, name , ssn

class Patient:

    def setId(self, id):
        self.id = id
    def getId(self):
        return self.id
    
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def setSSN(self, ssn):
        self.ssn = ssn
    def getSSN(self):
        return self.ssn

    def displayP(self):
        print(self.getId())
        print(self.getName())
        print(self.getSSN())

    
p = Patient()
p.setId(21)
p.setName('Krish')
p.setSSN(123456)

p.displayP()
# print(p.getId())
# print(p.getName())
# print(p.getSSN())