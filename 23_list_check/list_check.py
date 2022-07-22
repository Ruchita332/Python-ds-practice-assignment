def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for item in lst:
        if (isinstance (item, list) is not True):
            return False;

    return True;

    # Alternate possibilities: use all() with a generator comprehension,
    # though that isn't something we've covered yet:
    #
    # return all(isinstance(item, list) for item in lst)
