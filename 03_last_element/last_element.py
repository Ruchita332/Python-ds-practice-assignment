def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    # if (len(lst)):
    if lst:
        return lst[-1];
    
    # As it returns none by default
    # else:
    #     return None
