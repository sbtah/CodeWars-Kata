# The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

# To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.


data = [(18, 20), (45, 2), (61, 12), (37, 6), (21, 21), (78, 9)]

def open_or_senior(data):

    newList = []

    for val in data:
        if val[0] > 55 and val[1] > 7:
            newList.append("Senior")
        else:
            newList.append("Open")
        
    return newList

print(open_or_senior(data))