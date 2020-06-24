#2.1
def slice_reverse(s, i, j):
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> slice_reverse(s, 1, 2)
    >>> s
    Link(1, Link(2, Link(3)))
    >>> s = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> slice_reverse(s, 2, 4)
    >>> s
    Link(1, Link(2, Link(4, Link(3, Link(5)))))
    """
    start = s
    for _ in range(i):
        start = start.rest
    reverse = Link.empty
    current = start
    for _ in range(j - i):
        
        current.rest = _____________________________________________
        reverse = Link
        current = __________________________________________________
    ____________________________________________________________
    ____________________________________________________________
    ____________________________________________________________
