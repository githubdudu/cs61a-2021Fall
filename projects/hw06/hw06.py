class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    def __init__(self, good_name, price):
        self.good_name = good_name
        self.price = price
        self.stock = 0
        self.funds = 0

    def vend(self):
        if self.stock <= 0:
            return 'Nothing left to vend. Please restock.'
        elif self.funds < self.price:
            return f'You must add ${self.price - self.funds} more funds.'
        else:
            change = self.funds - self.price
            self.funds = 0
            self.stock -= 1
            if change:
                return f'Here is your {self.good_name} and ${change} change.'
            else:
                return f'Here is your {self.good_name}.'

    def add_funds(self, amount):
        if self.stock <= 0:
            return f'Nothing left to vend. Please restock. Here is your ${amount}.'
        self.funds += amount
        return f'Current balance: ${self.funds}'

    def restock(self, amount):
        self.stock += amount
        return f'Current {self.good_name} stock: {self.stock}'

class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.

    >>> mint = Mint()
    >>> mint.year
    2021
    >>> dime = mint.create(Dime)
    >>> dime.year
    2021
    >>> Mint.present_year = 2101  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2021
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2101
    >>> Mint.present_year = 2176     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year = 2021

    def __init__(self):
        self.update()

    def create(self, kind):
        return kind(self.year)

    def update(self):
        self.year = Mint.present_year


class Coin:
    def __init__(self, year):
        self.year = year

    def worth(self):
        return self.cents + max((Mint.present_year - self.year - 50), 0)


class Nickel(Coin):
    cents = 5


class Dime(Coin):
    cents = 10


def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    >>> # a check for restricted functions
    >>> import inspect, re
    >>> cleaned = re.sub(r"#.*\\n", '', re.sub(r'"{3}[\s\S]*?"{3}', '', inspect.getsource(store_digits)))
    >>> print("Do not use str or reversed!") if any([r in cleaned for r in ["str", "reversed"]]) else None
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    """
    def link_left(n, start=Link.empty):
        left, right = n // 10, n % 10
        if left == 0:
            return Link(right, start)
        else:
            return link_left(left, Link(right, start))

    return link_left(n)


def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print(link1)
    <3 <4> 5 6>
    >>> # Disallow the use of making new Links before calling deep_map_mut
    >>> Link.__init__, hold = lambda *args: print("Do not create any new Links."), Link.__init__
    >>> try:
    ...     deep_map_mut(lambda x: x * x, link1)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(link1)
    <9 <16> 25 36>
    """
    if isinstance(link.first, Link):
        deep_map_mut(fn, link.first)
    elif isinstance(link.first, int):
        link.first = fn(link.first)
    
    if isinstance(link.rest, Link):
        deep_map_mut(fn, link.rest)
    elif isinstance(link.rest, int):
        link.rest = fn(link.rest)


def two_list(vals, amounts):
    """
    Returns a linked list according to the two lists that were passed in. Assume
    vals and amounts are the same size. Elements in vals represent the value, and the
    corresponding element in amounts represents the number of this value desired in the
    final linked list. Assume all elements in amounts are greater than 0. Assume both
    lists have at least one element.

    >>> a = [1, 3, 2]
    >>> b = [1, 1, 1]
    >>> c = two_list(a, b)
    >>> c
    Link(1, Link(3, Link(2)))
    >>> a = [1, 3, 2]
    >>> b = [2, 2, 1]
    >>> c = two_list(a, b)
    >>> c
    Link(1, Link(1, Link(3, Link(3, Link(2)))))
    """
    if len(amounts) == 0:
        return Link.empty

    if amounts[0] == 1:
        return Link(vals[0], two_list(vals[1:], amounts[1:]))
    else:
        amounts[0] -= 1
        return Link(vals[0], two_list(vals, amounts))


class VirFib():
    """A Virahanka Fibonacci number.

    >>> start = VirFib()
    >>> start
    VirFib object, value 0
    >>> start.next()
    VirFib object, value 1
    >>> start.next().next()
    VirFib object, value 1
    >>> start.next().next().next()
    VirFib object, value 2
    >>> start.next().next().next().next()
    VirFib object, value 3
    >>> start.next().next().next().next().next()
    VirFib object, value 5
    >>> start.next().next().next().next().next().next()
    VirFib object, value 8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    VirFib object, value 8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        if hasattr(self, 'prev'):
            res = VirFib(self.value + self.prev)
        else:
            res = VirFib(self.value + 1)
        res.prev = self.value
        return res

    def __repr__(self):
        return "VirFib object, value " + str(self.value)


def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    """
    1. Each node has at most two children (a leaf is automatically a valid binary search tree)
    2. The children are valid binary search trees
    3. For every node, the entries in that node's left child are less than or equal to the label of the node
    4. For every node, the entries in that node's right child are greater than the label of the node
    5. Note that, if a node has only one child, that child could be considered either the left or right child. You should take this into consideration.
    """
    # is_leaf
    if t.is_leaf():
        return True
    # at most two children
    if len(t.branches) > 2:
        return False
    # one child
    if len(t.branches) == 1:
        return is_bst(t.branches[0])
    if bst_max(t.branches[0]) <= t.label < bst_min(t.branches[1]):
        return is_bst(t.branches[0]) and is_bst(t.branches[1])
    else:
        return False

def bst_min(t):
    """
    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> bst_min(t1)
    1
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> bst_min(t4)
    1
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> bst_min(t5)
    -2
    """
    if t.is_leaf():
        return t.label
    if len(t.branches) == 1:
        return min(t.label, bst_min(t.branches[0]))
    else:
        return bst_min(t.branches[0])

def bst_max(t):
    """
    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> bst_max(t1)
    8
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> bst_max(t4)
    4
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> bst_max(t5)
    1
    """
    if t.is_leaf():
        return t.label
    if len(t.branches) == 1:
        return max(t.label, bst_max(t.branches[0]))
    else:
        return bst_max(t.branches[1])

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
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


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()
