def create_solution_functions():
    import sympy
    from sympy import Symbol, Function, log, sympify

    n = Symbol('n')
    O = Function('O')

    solutions = {
        "1_0" : O(n* log(n)),
        "1_1" : O(1),
        "1_2" : O(n),
        "1_3" : O(n**2),
        "1_4" : O(n*log(n)),
        "1_5" : O((n**3)* log(n)),
        "1_6" : O(n**2),
        "1_7" : O(n**2),
        "1_8" : O(n),
        "2_0" : O(n),
        "2_1" : O(1),
        "2_2" : O(n),
        "2_3" : O(n),
        "2_4" : O(n**2),
        "2_5" : O(n**3),
        "2_6" : O(n**2),
        "2_7" : O(log(n)),
        "2_8" : O(n * log(n)),
        "5_1" : O(n),
    }


    def make_solution_function(correct_answer):
        def solution_function(answer):
            import math
            n = Symbol('n')
            answer = sympify(answer).replace(O, lambda x: x)
            correct = correct_answer.replace(O, lambda x: x)
            if correct.equals(answer):
                print("Test case passed!")
                return

            results = []
            for exp in range(10, 110, 10):
                val = 10 ** exp
                ratio = (answer.subs(n, val) / correct.subs(n, val))
                results.append(log(ratio).evalf())
            inf, sup = min(results), max(results)
            if math.isclose(inf, sup):
                if math.isclose(inf, 0):
                    print("Test case passed!")
                else:
                    print("---------------- Test case failed. ----------------")
                    print(f"Very close! The answer you provided, {repr(answer)},")
                    print("differs from the correct answer by a constant factor.")
                    print("---------------------------------------------------")
                    print()
            else:
                print("---------------- Test case failed. ----------------")
                if results[-1] < 1:
                    print(f"The answer you provided, {repr(answer)}, grows ")
                    print("more slowly than the correct answer.")
                elif results[-1] > 1:
                    print(f"The answer you provided, {repr(answer)}, grows ")
                    print("more quickly than the correct answer.")
                print("---------------------------------------------------")
                print()
        return solution_function

    # globals_ = globals()
    for question, solution in solutions.items():
        name = f"check_answer{question}"
        fn = make_solution_function(solution)
        fn.__name__ = name
        globals()[name] = fn
        print("Modified function:", name in globals())

   

def check_answer3(name, n):
    import math
    if name != "Zaria":
        print("One of 3.1 and 3.2 is incorrect :(")
        return

    if 0.0001 * (n ** 2) >= 10 * n * math.log(n):
        print("One of 3.1 and 3.2 is incorrect :(")
        return

    print("Both 3.1 and 3.2 are correct! :)")


create_solution_functions()