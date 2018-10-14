class Number:
    """This is how numbers and units are contained"""
    #Initializing numbers
    def __init__(self, quantity=None, unit=None):
        self.numbers = []
        if quantity!=None and unit != None:
            self.add_item(quantity,unit)
        elif unit != None:
            self.add_item(1,unit)
        elif quantity != None:
            self.add_item(quantity,"")
    #Containing and manually setting numbers
    def set_number(self, quantity=1, unit=""):
        self.numbers=[]
        self.add_item(quantity, unit)

    def append_number(self, number=1, unit=""):
        self.add_item(number, unit)

    def add_item(self, quantity, unit):
        self.numbers.append({"quantity":quantity, "unit": unit})

    def list_units(self):
        l = []
        for n in self.numbers:
            l.append(n["unit"])
        return l

    def remove_index(self, index):
        self.numbers.pop(index)

    def copy_number(self):
        copy = Number()
        for n in self.numbers:
            copy.add_item(n["quantity"], n["unit"])
        return copy

    def __str__(self):
        ret=""
        for n in self.numbers:
            ret+= str(n["quantity"]) + n["unit"] + " + "
        if len(ret) > 3:
            return ret[:-3]
        return ""

    #Arithmetic operations on numbers
    def add(self, number):
        copy = self.copy_number()
        units=copy.list_units()
        for n in number.numbers:
            if n["unit"] not in units:
                copy.numbers.append(n)
            else:
                for toadd in copy.numbers:
                    if toadd["unit"] == n["unit"]:
                        toadd["quantity"]+=n["quantity"]
        return copy

    def subtract(self, number):
        negative=Number()
        for n in number.numbers:
            negative.append_number(n["quantity"] * -1, n["unit"])
        return self.add(negative)

    def multiply(self, number):
        copy = Number()
        for n in self.numbers:
            for n2 in number.numbers:
                copy.append_number(n["quantity"] * n2["quantity"], n["unit"] + n2["unit"])
        return copy

n1=Number(4, "x")
n1.append_number(4)
n2=Number(4)
n2.append_number(4, "y")
n1.add(n2)
#print(n1.numbers)
#print(n2.numbers)
print(n1)
