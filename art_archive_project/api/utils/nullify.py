def nullify(val):
    """
    Return None if value is empty string
    Intended to use for input value refinement
    """
    return val if val != "" else None
