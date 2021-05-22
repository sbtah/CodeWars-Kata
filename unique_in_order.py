def unique_in_order(string):
    """
    Returns a list of items without any elements with the same value next to each other.
    Also preserving the original order of elements.
    """
    previous_value = None #This tracks if element was seen before.
    new_list = []
    for element in string:
        if element != previous_value:
            new_list.append(element)
            previous_value = element
    
    return new_list

print(unique_in_order("AAAABBBCCDAABBB"))
print(unique_in_order('ABBCcAD'))
print(unique_in_order("a"))