#Link
class Link:
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


#1.1
a = Link(1, Link(2, Link(3)))

#1.2
def skip(lst):
    """
    >>> a = Link(1, Link(2, Link(3, Link(4))))
    >>> a
    Link(1, Link(2, Link(3, Link(4))))
    >>> b = skip(a)
    >>> b
    Link(1, Link(3))
    >>> a
    Link(1, Link(2, Link(3, Link(4)))) # Original is unchanged
    """
    if lst == Link.empty or lst.rest == Link.empty:
        return Link.empty
    else:
        return Link(lst.first, skip(lst.rest.rest))

#1.3
def skip(lst):
    """
    >>> a = Link(1, Link(2, Link(3, Link(4))))
    >>> b = skip(a)
    >>> b
    None
    >>> a
    Link(1, Link(3))
    """

    if lst == Link.empty or lst.rest == Link.empty:
        return None
    else:
        lst.rest = lst.rest.rest
        skip(lst.rest)

#1.4
def reverse(lst):
    """
    >>> a = Link(1, Link(2, Link(3)))
    >>> b = reverse(a)
    >>> b
    Link(3, Link(2, Link(1)))
    >>> a
    Link(1, Link(2, Link(3)))
    """
    if lst == Link.empty:
        return Link.empty
    elif lst.rest == Link.empty:
        return lst
    else:
        return append(reverse(lst.rest), lst.first)

def append(lst, x):
    if lst == Link.empty:
        return Link(x)
    else:
        return Link(lst.first, append(lst.rest, x))


#Tree
class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        self.branches = branches
        
    def is_leaf(self):
        return not self.branches
    
    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.label, branches_str)
    
#2.1
def contains(elem, n, t):
    """
    >>> t1 = Tree(1, [Tree(1, [Tree(2)])])
    >>> contains(1, 2, t1)
    True
    >>> contains(2, 2, t1)
    False
    >>> contains(2, 1, t1)
    True
    >>> t2 = Tree(1, [Tree(2), Tree(1, [Tree(1), Tree(2)])])
    >>> contains(1, 3, t2)
    True
    >>> contains(2, 2, t2) # Not on a path
    False
    """
    if n == 0:
        return True
    elif t.is_leaf():
        return n == 1 and t.label == elem
    elif t.label == elem:
        return True in [contains(elem, n-1 , b) for b in t.branches]
    else:
        return True in [contains(elem, n , b) for b in t.branches]

#2.2
def factor_tree(n):
    for i in range(2, n-1):
        if n % i == 0:
            return Tree(n, [factor_tree(i), factor_tree(n // i)])
    return Tree(n)

#2.3
earth = [0]
earth.append([earth])

def wind(fire, groove):
    fire[1][0][0] = groove
    def fire():
        nonlocal fire
        fire = lambda fantasy: earth.pop(1).extend(fantasy)
        return fire(groove)
    return fire()

sep = earth[1]
wind(earth, [earth[0]] + [earth.append(0)])
