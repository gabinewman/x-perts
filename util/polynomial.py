from term import Term
class Polynomial:
    """This is how numbers and units are contained"""

    # store express as a dictionary of terms indexed by their variable
    #Initializing numbers
    def __init__(self):
        self.terms = []

    def add_term(self, num):
        i = 0
        while i < len(self.terms):
            if (num.combineable(self.terms[i])):
                self.terms[i] = num.combine(self.terms[i])
                return;
            i += 1
        else:
            self.terms.append(num)

    def remove_index(self, index):
        self.terms.pop(index)

    def clean(self): # removes 0s
        i = 0
        while i < len(self.terms):
            if self.terms[i].coefficient == 0:
                self.terms.pop(i)
            i += 1


    def __str__(self):
        self.clean()
        if (len(self.terms) == 0):
            return ""
        retstr = str(self.terms[0])
        i = 1
        while i < len(self.terms):
            retstr += " "
            if (self.terms[i].coefficient < 0):
                copy = self.terms[i].copy()
                copy.coefficient = abs(copy.coefficient)
                retstr += "- " + str(copy)
            else:
                retstr += "+ " + str(self.terms[i])
            i += 1
        return retstr

exp = Polynomial()
vars1 = {"x":2}
vars2 = {"x":1, "y":1}
vars3 = {"x":2}
vars4 = {"q" : 0}
t = [Term(12, vars1), Term(1, vars2), Term(-13, vars3), Term(6, vars4)]
for term in t:
    exp.add_term(term)
    print(term)
print(exp)
