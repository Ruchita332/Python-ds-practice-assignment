def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    swapped_phrase = "";

    for ltr in phrase:
        if ltr.lower() == to_swap.lower():
            # there is a match swap the letter
            ltr = ltr.swapcase();
        swapped_phrase +=ltr;

    return swapped_phrase;



