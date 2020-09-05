def regex_func(pattern, search_str):
    """
    Function that cycles through a regex pattern and search string to see if it can find the
    pattern in the search string.  If it does, the function returns True. If it doesn't the
    function returns False.
    """
    if not pattern:
        return True
    if not search_str:
        return False
    if pattern[0] == search_str[0] or pattern[0] == '.':
        return regex_func(pattern[1:], search_str[1:])
    else:
        return regex_func(pattern, search_str[1:])


def search_strings():
    """
    Function that asks the user for a search pattern and search string and passes the two to
    the regex_function.  It returns a True or False value
    """
    regex, search = input().split('|')
    if regex_func(regex, search):
        return True
    else:
        return False


print(search_strings())
