def regex_func(pattern, search_str):
    if not pattern:
        return True
    if not search_str:
        return False
    if pattern[0] == search_str[0] or pattern[0] == '.':
        return regex_func(pattern[1:], search_str[1:])
    else:
        return False


regex, search = input().split('|')
print(regex_func(regex, search))
