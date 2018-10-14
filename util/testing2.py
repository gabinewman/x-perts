def parse_string(string_to_test):
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
    string_to_test = string_to_test.replace(' ( ',' ( ');
    string_to_test = string_to_test.replace('( ',' ( ');
    string_to_test = string_to_test.replace(' (',' ( ');
    string_to_test = string_to_test.replace('(',' ( ');
    string_to_test = string_to_test.replace(' ) ',' ) ');
    string_to_test = string_to_test.replace(') ',' ) ');
    string_to_test = string_to_test.replace(' )',' ) ');
    string_to_test = string_to_test.replace(')',' ) ');
    string_split = string_to_test.split();

    for element in string_split:
        try:
            i = float(element);
            variable.append(i);
        except:
            variable.append(element);


    return variable;
