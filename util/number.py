class Number:
    """This is how numbers and units are contained"""
    #Initializing numbers
    def __init__(self, quantity=None, unit=None):
        self.numbers = []
        if quantity!=None and unit != None:
            self.add_item(quantity,unit)
        elif quantity == None:
            self.add_item(1,unit)
        elif unit == None:
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
    def __str__(self):
        ret=""
        for n in self.numbers:
            ret+= str(n["quantity"]) + n["unit"] + " + "
        if len(ret) > 3:
            return ret[:-3]
        return ""
    #Arithmetic operations on numbers
    def add(self, number):
        units=self.list_units()
        for n in number.numbers:
            if n["unit"] not in units:
                self.numbers.append(n)
            else:
                for toadd in self.numbers:
                    if toadd["unit"] == n["unit"]:
                        toadd["quantity"]+=n["quantity"]

n1=Number(4, "x")
n1.append_number(4)
n2=Number(2)
n2.append_number(7, "y")
n1.add(n2)
print(n1)
