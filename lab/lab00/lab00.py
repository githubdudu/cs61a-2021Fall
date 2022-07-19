def twenty_twenty_one():
    """Come up with the most creative expression that evaluates to 2021,
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty_one()
    2021
    """
    x = 1
    def inner_fun():
        nonlocal x
        x += 1
        print(x)
    return inner_fun
