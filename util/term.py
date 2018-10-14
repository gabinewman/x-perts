class Term:
    # has a "coefficient" variable that is a float, and a "variable" variable that is an instance of Variable

    #Initializing term
    def __init__(self, coefficient=None, variables=None): #takes coefficient and dictionary of exponents (indexed by their base) to create new term
        if (coefficient is None):
            self.coefficient = 0.0
        else:
            self.coefficient = coefficient
        if (variables is None):
            self.variables = {}
        else:
            self.variables = variables

    def copy(self):
        variables_copy = {}
        for k in self.variables:
            variables_copy[k] = self.variables[k]
        return Term(self.coefficient, variables_copy)

    def __str__(self):
        retstr = ""
        if abs(self.coefficient) != 1:
            retstr += str(self.coefficient)
        elif self.coefficient == -1:
            retstr += "-"
        keys = sorted(self.variables.keys())
        for base in keys:
            if (self.variables[base] > 1):
                retstr += base + "^" + str(self.variables[base])
            elif (self.variables[base] == 1):
                retstr += base
            else:
                continue
        return retstr

    def is_constant(self):
        return self.variables.keys.len == 0

    # combines two like terms; other must have variable component that is equal to self's variable component
    def combine(self, other):
        copy = self.copy()
        copy.coefficient += other.coefficient
        return copy

    def multiply(self, other):
        copy = Term()
        copy.coefficient = self.coefficient * other.coefficient
        for base in self.variables:
            if (base in other.variables.keys()): # combine common bases
                copy.variables[base] = self.variables[base] + other.variables[base]
            else: # add bases unique to self.variables
                copy.variables[base] = self.variables[base]
        for base in other.variables: # add bases unique to other.variables
            if (base not in self.variables.keys()):
                copy.variables[base] = other.variables[base]
        return copy

    def combineable(self, other):
        for base in self.variables:
            if (base not in other.variables.keys() or self.variables[base] != other.variables[base]):
                return False

        for base in other.variables:
            if (base not in self.variables.keys() or other.variables[base] != self.variables[base]):
                return False

        return True

"""vars1 = {"x": 1, "z": 2}
vars2 = {"y": 1, "z": 1}
term1 = Term(5, vars1)
print (term1)
term2 = Term(3, vars2)
print(term2)
sum = term1.multiply(term2)
print(sum)"""
