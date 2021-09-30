# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

def solution2(s):

    new_l = [] #opens new list and appends new elements into it.

    if len(s) % 2 != 0:#checks if test string is even or odd and adds underscore if it's odd.
        new_s = list(s+"_")
    else:
        new_s = list(s)
    
    for elem in range(len(new_s)):
        previous = new_s[elem] #tracks last looped item
        if elem % 2 != 0: #checks if element is not even
            new_l.append(new_s[elem-1] + previous)#appends two items joined into string; 

    return new_l
           

   

    

print(solution2('missing'))