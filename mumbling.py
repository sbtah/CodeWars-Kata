#This time no story, no theory. The examples below show you how to write function accum:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"


def accum(s):
	"""
	Returns new string generated from s, where all elements are multiplied by element's position number.
	Also 1st symbol of new string is capitalized and elements are seperated by dashes.
	ie: from "abcd" -> A-Bb-Ccc-Dddd"
	"""
	new_list = []
	for i, element in enumerate(s):
		new_list.append(element * (i + 1))
		new_s = "-".join(new_list).title()
	return new_s


print(accum("abcd"))