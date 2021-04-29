# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.


def xo(s):
	s = s.lower()
	if s.count("x") == s.count("o"):
		return True
	else:
		return False


print(xo("xooxx"))
print(xo("ooxx"))