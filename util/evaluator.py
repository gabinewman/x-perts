
#  the operators + and - have a precedence of 1, while the operators * and / have a precedence of 2
"""1. If we encounter an operator token in the input and the operator stack is empty,
we push the operator token onto the operator stack.
2. If we encounter an operator token in the input with a precedence that is greater than the precedence of the operator token
at the top of the operator stack, we push the new operator token onto the operator stack.
3. If we encounter an operator token in the input with a precedence that is less than or equal to the precedence
of the operator at the top of the stack, we process and remove the operator at the top of the stack.
4. This continues until the operator stack is empty or until an operator with lower precedence than the input operator appears
at the top of the stack.
5. When we reach the end of the input, any operators that remain on the operator stack are processed and removed until
the operator stack is empty.
6. At that point, there should be only one number token left on the value stack: that number is the result of the evaluation."""

""" 1. When we encounter a left parentheses token in the input, we push that token on the operator stack.
2. When we encounter a right parenthesis token in the input, we process operators and remove them from the
top of the operator stack until a left parenthesis appears at the top of the operator stack.
3. We then pop off the left parenthesis token and discard both of the parenthesis tokens."""



from stack import Stack
from number import Number

operators = Stack()
values = Stack()

def evaluate_stack(tokens):
    for token in tokens:
        if (type(token) == float or type(token) == int):
            values.push(token)
        elif (token == "("):
            operators.push("(")
        elif (token == ")"):
            while (operators.peek() != "("): #keep processing operations in stack until you reach left paren
                process_operator()
            operators.pop()
        elif (token == "+" or token == "-"):
            # case 1: stack is empty or the top operator is a left paren
            if (operators.size() == 0 or operators.peek() == "("): # shouldn't throw exception due to short-circuiting
                operators.push(token)
            # case 2: there is another operator on top of the stack
            else:
                while (operators.size() > 0 and operators.peek() != "("): # also shouldn't except bc short-circuiting
                    process_operator() # keep processing operations in stack until you reach bottom of stack or left paren
                operators.push(token)
        elif (token == "*" or token == "/"):
            # case 1: stack is empty, the top operator is a left paren, or the top operator is +/-
            if (operators.size() == 0 or operators.peek() in "+-)"):
                operators.push(token)
            # case 2: the top operator is / or *
            else:
                while (operators.size() > 0 and operators.peek() not in "+-("):
                    process_operator()
                operators.push(token)

    while (operators.size() > 0):
        process_operator()

    return values.pop()


# precon: there is a valid operator at the top of the stack
def process_operator():
    operator = operators.pop()
    y = values.pop()
    x = values.pop()
    if operator == "+":
        values.push(x + y)
    elif operator == "-":
        values.push(x - y)
    elif operator == "*":
        values.push(x * y)
    else:
        values.push(x /  float(y))

# takes float and returns a Number representation of that float
def convent_to_Number(f):
    num = Number(f)


def is_operator(x):
    return x in "+-*/"
