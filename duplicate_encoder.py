# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.


def duplicate_encode(word):
	data = list(word.lower())
	res = []
	for item in data:
		if data.count(item) == 1:
			res.append(item.replace(item, "("))
		elif data.count(item) > 1:
			res.append(item.replace(item, ")"))
	return "".join(res)


print(duplicate_encode("recede"))
print(duplicate_encode("Success"))

