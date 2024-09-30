def modify_string():
    s = "rummy"
    position = 0
    character = 'd'
    string_list = list(s)
    string_list[position] = character
    modified_string = ''.join(string_list)

    return modified_string
result=modify_string()
print(result)


