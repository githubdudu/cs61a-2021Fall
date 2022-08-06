class Pair:
    """Represents the built-in pair data structure in Scheme."""
    def __init__(self, first, rest):
        self.first = first
        if not scheme_valid_cdrp(rest):
            raise SchemeError("cdr can only be a pair, nil, or a promise but was {}".format(rest))
        self.rest = rest

    def map(self, fn):
        """Maps fn to every element in a list, returning a new
        Pair.

        >>> Pair(1, Pair(2, Pair(3, nil))).map(lambda x: x * x)
        Pair(1, Pair(4, Pair(9, nil)))
        """
        assert isinstance(self.rest, Pair) or self.rest is nil, \
            "rest element in pair must be another pair or nil"
        return Pair(fn(self.first), self.rest.map(fn))

    def __repr__(self):
        return 'Pair({}, {})'.format(self.first, self.rest)
class nil:
    """Represents the special empty pair nil in Scheme."""
    def map(self, fn):
        return nil
    def __getitem__(self, i):
         raise IndexError('Index out of range')
    def __repr__(self):
        return 'nil'

nil = nil() # this hides the nil class *forever*


Answer the following questions about a Pair instance representing the Calculator expression (+ (- 2 4) 6 8).

Write out the Python expression that returns a Pair representing the given expression:
Pair('+', Pair((Pair('-'), Pair(2, Pair(4, nil))), Pair(6, Pair(8, nil))))

What is the operator of the call expression?
'+'

If the Pair you constructed in the previous part was bound to the name p, how would you retrieve the operator?
p.first

What are the operands of the call expression?
(- 2 4) 6 8

If the Pair you constructed was bound to the name p, how would you retrieve a list containing all of the operands?
p.rest  recursion function

How would you retrieve only the first operand?
p.rest.first 
