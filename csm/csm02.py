#3
def all_primes(nums):

    return [n for n in nums if is_prime(n)]

#4
def list_of_lists(lst):
    """
    >>> list_of_lists([1, 2, 3])
    [[0], [0, 1], [0, 1, 2])
    >>>list_of_lists([1])
    [[0]]
    >>>list_of_lists([])
    []
    """
    return [list(range(n)) for n in lst]

#Things to remember!
def tree(label, branches=[]):
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:] #returns a list of branches

def is_leaf(tree):
    return branches(tree) == []

#Trees
t = tree(9, [tree(2), tree(4, [tree(1)]), tree(4, [tree(7), tree(3)])])

#3
branches(t)[0][0]

#4
def sum_of_nodes(t):
    """
    >>> t = tree(...) # Tree from question 2.
    >>> sum_of_nodes(t) # 9 + 2 + 4 + 4 + 1 + 7 + 3 = 30
    30
    """
    def all_nodes(t):
        if is_leaf(t):
            return tree(label(t))
        else:
            return sum([all_nodes(branch) for branch in branches(t)], tree(label(t)))
    return sum(all_nodes(t))
