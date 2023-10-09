def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    # true_lst = []

    # for itm in lst:
    #     if itm:
    #         true_lst.append(itm)
    # return true_lst

    return [itm for itm in lst if itm]