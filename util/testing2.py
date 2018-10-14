string_to_test = "3+ 5+ 10";
variable = [];

string_to_test = string_to_test.replace("+"," + ");
string_to_test = string_to_test.replace('+ ',' + ');
string_to_test = string_to_test.replace(' +',' + ');
string_to_test = string_to_test.replace('+',' + ');
string_to_test = string_to_test.replace(' - ',' - ');
string_to_test = string_to_test.replace('- ',' - ');
string_to_test = string_to_test.replace(' -',' - ');
string_to_test = string_to_test.replace('-',' - ');
string_to_test = string_to_test.replace(' / ',' / ');
string_to_test = string_to_test.replace('/ ',' / ');
string_to_test = string_to_test.replace(' /',' / ');
string_to_test = string_to_test.replace('/',' / ');
string_to_test = string_to_test.replace(' * ',' * ');
string_to_test = string_to_test.replace('* ',' * ');
string_to_test = string_to_test.replace(' *',' * ');
string_to_test = string_to_test.replace('*',' * ');

string_split = string_to_test.split();

for element in string_split:
    try:
        i = float(element);
        variable.append(i);
        print(variable);
    except:
        variable.append(element);


print(variable);
