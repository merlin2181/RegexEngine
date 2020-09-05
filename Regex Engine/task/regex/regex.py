def regex_func():
    regex, search_str = input().split('|')
    # if not regex and not search_str:
        # return False
    if regex in search_str or not regex:
        return True
    if regex == '.' and len(search_str) == 1:
        return True
    if not search_str or regex not in search_str:
        return False


print(regex_func())
