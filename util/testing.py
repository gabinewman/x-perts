string_to_test = "3 + 5+ * 10";
string_split = string_to_test.split();
variable = [];



for element in string_split:
    try:
        i = float(element);
        variable.append(i);
        print(variable);
    except:
        variable.append(element);


print(variable);
