#1.2
def foo():
	a = 0
	while a < 10:
		print("Hello")
		yield a
		a += 1
		print("World")

#1.3
def hailstone_sequence(n):
    """
    >>> hs_gen = hailstone_sequence(10)
    >>> next(hs_gen)
    10
    >>> next(hs_gen)
    5
    >>> for i in hs_gen:
    print(i)
    16
    8
    4
    2
    1
    """
    while n != 1:
        yield n
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
    yield 1

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
    
#1.4
def tree_sequence(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(5)]), Tree(3, [Tree(4)])])
    >>> print(list(tree_sequence(t)))
    [1, 2, 5, 3, 4]
    """
    if t.is_leaf():
        yield t.label
    else:
        yield t.label
        for b in t.branches:
            yield from tree_sequence(b)

#4.1
def all_paths(t):
        """
        >>> t = Tree(1, [Tree(2, [Tree(5)]), Tree(3, [Tree(4)])])
        >>> print(list(all_paths(t)))
        [[1, 2, 5], [1, 3, 4]]
        """
        if t.is_leaf():
                yield [t.label]
        for b in t.branches:
                for p in all_paths(b):
                        yield [t.label] + p
