# Constructor
def tree(label, branches=[]):
    return [label] + list(branches)

# Selectors
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

# For convenience
def is_leaf(tree):
    return not branches(tree)

# 3.1
def all_labels(t):
    if is_leaf(t):
        return [label(t)]
    else:
        return sum([all_labels(branch) for branch in branches(t)],[label(t)])

def tree_max(t):
    """Return the max of a tree."""
    return max(all_labels(t))

def height(t):
    """Return the height of a tree"""
    if is_leaf(t):
        return 0
    else:
        return 1 + max(height(branch) for branch in branches(t))

def square_tree(t):
    """Return a tree with the square of every element in t"""
    if is_leaf(t):
        return [label(t)**2]
    else:
        return tree(label(t)**2,[square_tree(branch) for branch in branches(t)])

def find_path(t, x):
    """
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    def find(t, x):
        if label(t) == x:
                return [x]
        else:
            for branch in branches(t):
                if x in all_labels(branch):
                    return [label(t)] + find(branch, x)
    if x in all_labels(t):
        return find(t, x)
    else:
        return None

def prune(t, k):
    if k == 0:
        return [label(t)]
    else:
        return tree(label(t), [prune(branch, k-1) for branch in branches(t)])

t = tree(1,[tree(3,[tree(4),tree(5),tree(6)]),tree(2)])
