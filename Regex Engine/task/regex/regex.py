def match_func(pattern, search_str):
    """
    Function that cycles through a regex pattern and search string to see if it can find the
    pattern in the search string.  If it does, the function returns True. If it doesn't the
    function returns False.
    :pattern: the pattern to search for in the user inputted search string
    :search_str: the user inputted search string
    :return: True, False or goes into recursion offsetting either both the pattern and search_str or just the search_str
    """
    if not pattern:
        return True
    if not search_str:
        return False
    if pattern[0] == search_str[0] or pattern[0] == '.':
        return match_func(pattern[1:], search_str[1:])
    else:
        return match_func(pattern, search_str[1:])


def carat(pattern, search_str):
    """
    Function that checks for an occurrence related to a character(s) with a '^'
    before it and continues to parse the search string
    :pattern: the pattern to search for in the user inputted search string
    :search_str: the user inputted search string
    :return: False, a comparison if '$' is present, search_strings function if another wildcard is present or
            the match_func function is there are no other wildcards present
    """
    pattern = pattern[1:]
    for item in wildcards:
        if item in pattern:
            if item == '$':
                index = pattern.index(item)
                pattern = pattern[:index]
                return pattern == search_str
            else:
                index = pattern.index(item)
                pattern_one = pattern[:index - 1]
                if match_func(pattern_one, search_str[:len(pattern_one)]):
                    return func_dict[item](pattern[len(pattern_one):], search_str[len(pattern_one):])
                else:
                    return False
    return match_func(pattern, search_str[:len(pattern)])


def keene_plus(pattern, search_str):
    """
    Function that checks for one or more occurrences related to a character with a '+'
    after it and continues to parse the search string
    :pattern: the pattern to search for in the user inputted search string
    :search_str: the user inputted search string
    :return: False or the check_one_or_more function to further parse the search_str
    """
    index = pattern.index('+')
    char = pattern[index - 1]
    if search_str.count(char) == 0 and char != '.':
        return False
    else:
        return check_one_or_more(pattern, search_str, char)


def keene_star(pattern, search_str):
    """
    Function that checks for zero or more occurrences related to a character with a '*'
    after it and continues to parse the search string
    :pattern: the pattern to search for in the user inputted search string
    :search_str: the user inputted search string
    :return: The search_strings function if there is no character or the check_one_or_more function if there is
    """

    index = pattern.index('*')
    char = pattern[index - 1]
    if search_str.count(char) == 0 and char != '.':
        pattern_one = pattern[:index - 1] + pattern[index + 1:]
        return search_strings(pattern_one, search_str)
    else:
        return check_one_or_more(pattern, search_str, char)


def keene_mark(pattern, search_str):
    """
    Function that checks for zero or one occurrence related to a character with a '?'
    after it and continues to parse the search string
    :pattern: the pattern to search for in the user inputted search string
    :search_str: the user inputted search string
    :return: False or the search_strings function to further parse the search_str
    """
    index = pattern.index('?')
    char = pattern[index - 1]
    if search_str.count(char) > 1:
        return False
    if search_str.count(char) == 1:
        pattern_one = pattern[:index] + pattern[index + 1:]
        return search_strings(pattern_one, search_str)
    if search_str.count(char) == 0:
        pattern_two = pattern[:index - 1] + pattern[index + 1:]
        return search_strings(pattern_two, search_str)


def dollar_sign(pattern, search_str):
    """
    Function that checks one or more occurrences related to a character with a '+' or '*'
    after it and continues to parse the search string
    :pattern: the pattern to search for in the user inputted search string
    :search_str: the user inputted search string
    :return: False or the match_func function to further parse the search_str
    """
    index = pattern.index('$')
    if index == 0 and len(search_str) > 0:
        return False
    return match_func(pattern[:index], search_str[-index:])


def check_one_or_more(pattern, search_str, char):
    """
    Function that checks one or more occurrences related to a character with a '+' or '*'
    after it and continues to parse the search string
    :pattern: the pattern to search for in the user inputted search string
    :search_str: the user inputted search string
    :char: the character we are looking for to occur one or multiple times
    :return: True, False or the search_strings function to further parse the search_str
    """
    if char != '.':
        pattern_index = pattern.index(char)
        search_index = search_str.index(char)
        if pattern_index != search_index:
            return False
        else:
            if match_func(pattern[:pattern_index], search_str[:search_index]):
                search_str = search_str[search_index:]
                while search_str[0] == char:
                    search_str = search_str[1:]
                try:
                    pattern = pattern[pattern_index + 2:]
                except IndexError:
                    return len(pattern) < len(search_str)
                for item in wildcards:
                    if item in pattern:
                        return func_dict[item](pattern, search_str)
                return match_func(pattern, search_str)
    else:
        if pattern[-2] == char:
            return True
        else:
            pattern_index = pattern.index(char)
            pattern = pattern[pattern_index + 2:]
            return search_strings(pattern, search_str)


def search_strings(pattern, search_str):
    """
    Function that asks the user for a search pattern and search string, checks for
    metacharacters '^' and '$' and either passes the two to
    the match_function or checks the search string itself.  It returns a True or False value
    """
    for item in wildcards:
        if item in pattern:
            return func_dict[item](pattern, search_str)
    return match_func(pattern, search_str)


wildcards = ('^', '+', '?', '*', '$')
func_dict = {'^': carat,
             '$': dollar_sign,
             '?': keene_mark,
             '*': keene_star,
             '+': keene_plus}
regex, search = input().split('|')
print(search_strings(regex, search))
