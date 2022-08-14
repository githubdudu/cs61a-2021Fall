# i. Are we able to handle expressions containing the comparison operators (such as <, >, or =) with the existing implementation of calc_eval? Why or why not?
# Yes, we are. Same behavior with '+', '-'

# ii. Are we able to handle 'and' expressions with the existing implementation of calc_eval? Why or why not?
# No, we can't. 'and' apply short circuit.

# Hint: Think about the rules of evaluation we've implemented in calc_eval. Is anything different about and?



from Q1 import Pair, nil
from Q2 import OPERATORS

def calc_eval(exp):
    if isinstance(exp, Pair):
        if exp.first == 'and': # and expressions
            return eval_and(exp.rest)
        else:                   # Call expressions
            return calc_apply(calc_eval(exp.first), exp.rest.map(calc_eval))
    elif exp in OPERATORS:      # Names
        return OPERATORS[exp]
    else:                       # Numbers
        return exp

def eval_and(operands):
    init = True
    while init and operands is not nil:
        init = init and calc_eval(operands.first)
        operands = operands.rest
    return init

# Q4 -------------------------------------
bindings = {}
def calc_eval(exp):
    if isinstance(exp, Pair):
        if exp.first == 'and': # and expressions[paste your answer from the earlier]
            return eval_and(exp.rest)
        elif exp.first == 'define': # define expressions
            return eval_define(exp.rest)

        else:                   # Call expressions
            return calc_apply(calc_eval(exp.first), exp.rest.map(calc_eval))
    elif exp in bindings: # Looking up variables
        return bindings[exp]
    elif exp in OPERATORS:      # Looking up procedures
        return OPERATORS[exp]
    else:                       # Numbers
        return exp

def eval_define(expr):
    bindings[expr.first] = calc_eval(expr.rest.first)
    return expr.first

# Q5 ---------------------------------
# How many calls to calc_eval and calc_apply would it take to evaluate each of the following Calculator expressions?

scm> (+ 1 2)
For this particular prompt please list out the inputs to calc_eval and calc_apply.Your Answer:
calc_eval(Pair('+', Pair(1, Pair(2, nil))))
calc_apply('+', Pair(1, Pair(2, nil)))
calc_eval('+')
calc_eval(1)
calc_eval(2)
calc_eval(nil)
6 times

scm> (+ 2 4 6 8)
8 times

scm> (+ 2 (* 4 (- 6 8)))
6 + 5 + 5

scm> (and 1 (+ 1 0) 0)
calc_eval(exp)
calc_eval(1)
calc_eval((+ 1 0)) 6 times
calc_eval(0)


# Q6 ---------------------------------

>>> Pair('+', Pair(1, Pair(2, Pair(3, Pair(4, nil)))))
(+ 1 2 3 4)

>>> Pair('+', Pair(1, Pair(Pair('*', Pair(2, Pair(3, nil))), nil)))
(+ 1 (* 2 3))