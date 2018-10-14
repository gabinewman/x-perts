from testing2 import parse_string
from evaluator import *

def solve(problem):
    array = parse_string(problem)
    solution = evaluate_stack(array)
    return solution
