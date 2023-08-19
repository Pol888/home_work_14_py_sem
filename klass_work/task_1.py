def special_function(text: str):
    """
    >>> special_function("super mario")
    'super mario'
    >>> special_function("Super MARIo")
    'super mario'
    >>> special_function("Super, MARIo.")
    'super mario'
    >>> special_function("super marioсупермарио")
    'super mario'
    >>> special_function("supeR maRio,-супермарио")
    'super mario'
    """
    text = text.lower()
    for char in text:
        if ord(char) == 32 or 97 <= ord(char) <= 122:
            continue
        else:
            text = text.replace(char, '')

    return text


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
