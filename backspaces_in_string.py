# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"
# Your task is to process a string with "#" symbols.

import time
test_string = "a#bc#d"

def clean_string(s):
    
    ss = [x for x in s]
    
    while '#' in ss:
       for i in range(len(ss)):
            if i < len(ss)-1 and ss[i] == '#':
                del ss[i], ss[i-1]
                
                break

    return "".join(ss)

t = time.process_time()
print(clean_string(test_string))
elapsed_time = time.process_time() - t
print(elapsed_time)