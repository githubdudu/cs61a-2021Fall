from Q1 import Pair, nil



def calc_eval(exp):
    if isinstance(exp, Pair): # Call expressions
        return calc_apply(calc_eval(exp.first), exp.rest.map(calc_eval))
    elif exp in OPERATORS:      # Names
        return OPERATORS[exp]
    else:                       # Numbers
        return exp
        
def floor_div(expr):
    # do not need call calc_eval. Because calc_eval calls floor_div
    # data structure is based on Pair
    dividend = expr.first
    divisors = expr.rest
    while divisors is not nil:
        dividend = dividend // divisors.first
        divisors = divisors.rest
    return dividend

OPERATORS = {
    ['//']: floor_div
}

# Assume OPERATORS['//'] = floor_div is added for you in the code