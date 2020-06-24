#1.1
def stepper(num):
    def step():
        nonlocal num
        num = num + 1
        return num
    return step
s = stepper(3)
s()
s()

#1.2
lamb = 'da'
def da(da):
    def lamb(lamb):
        nonlocal da
        def da(nk):
            da = nk + ['da']
            da.append(nk[0:2])
            return nk.pop()
    da(lamb)
    return da([[1], 2]) + 3

a = da(lambda da: da(lamb))

#1.3
def memory(n):
    """
    >>> f = memory(10)
    >>> f = f(lambda x: x * 2)
    20
    >>> f = f(lambda x: x - 7)
    13
    >>> f = f(lambda x: x > 5)
    True
    """
    def use_f(f):
        nonlocal n
        print(f(n))
        return memory(f(n))
    return use_f

#2.2
def add_this_many(x, el, lst):
    """ Adds el to the end of lst the number of times x occurs
    in lst.
    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    for i in range(len(lst)):
        if x == lst[i]:
            lst.append(el)

#2.3
def reverse(lst):
    """ Reverses lst in place.
    >>> x = [3, 2, 4, 5, 1]
    >>> reverse(x)
    >>> x
    [1, 5, 4, 2, 3]
    """
    if len(lst) <= 1:
        return lst
    else:
        return reverse(lst[1:])+[lst[0]]

#3.2
def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    return {fn(x): [a for a in s if fn(a) == fn(x)] for x in s}

#3.3
def replace_all_deep(d, x, y):
    """
    >>> d = {1: {2: 'x', 'x': 4}, 2: {4: 4, 5: 'x'}}
    >>> replace_all_deep(d, 'x', 'y')
    >>> d
    {1: {2: 'y', 'x': 4}, 2: {4: 4, 5: 'y'}}
    """
    for key in d.keys():
        if type(d[key]) != type(dict()):
            if d[key] == x:
                d[key] = y
        else:
            replace_all_deep(d[key], x, y)

#3.4
