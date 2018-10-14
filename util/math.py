from util import testing2, evaluator

def solve(problem):
    try:
        print("hi")
        array = testing2.parse_string(problem)
        print(array)
        solution = evaluator.evaluate_stack(array)
        return solution
    except:
        return "error or solution not found"
