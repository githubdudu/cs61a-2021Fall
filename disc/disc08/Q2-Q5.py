
"""
ganondorf = Link('zelda', Link('link', Link('sheik', Link.empty)))
What expression would give us the value 'sheik' from this Linked List?
Your Answer:
'sheik' == ganondorf.rest.rest.first

What is the value of ganondorf.rest.first?

Your Answer:
'link'

What would be the value of str(ganondorf)?

Your Answer:
<zelda link sheik>

What expression would mutate this linked list to <zelda ganondorf sheik>?

Your Answer:
ganondorf.rest.first = 'ganondorf'
"""
class Link:
    """A linked list."""
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'



        
def sum_nums(s):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if s is Link.empty:
        return 0
    else:
        return s.first + sum_nums(s.rest)

def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Implementation Note: you might not need all lines in this skeleton code
    init = 1
    for link in lst_of_lnks:
        if link is Link.empty:
            return Link.empty
        init *= link.first
        
    lst_of_rest = [lnk.rest for lnk in lst_of_lnks]
    return Link(init, multiply_lnks(lst_of_rest))


def flip_two(s):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    if s is not Link.empty and s.rest is not Link.empty:
        s.first, s.rest.first = s.rest.first, s.first
        flip_two(s.rest.rest)
    # For an extra challenge, try writing out an iterative approach as well below!
    "*** YOUR CODE HERE ***"
    # while s is not Link.empty and s.rest is not Link.empty:
    #     s.first, s.rest.first = s.rest.first, s.first

    #     s = s.rest.rest
