# Given an array of numbers (in string format), you must return a string. The numbers correspond to the letters of the alphabet in reverse order: a=26, z=1 etc. You should also account for '!', '?' and ' ' that are represented by '27', '28' and '29' respectively.
# All inputs will be valid.


def switcher(arr):
	sample_string = " ?!abcdefghijklmnopqrstuvwxyz "[::-1]
	new_string = ""
	test_list = []
	for value in arr:
		test_list.append(int(value))
	for number in test_list:
		if number in range(len(sample_string)):
			new_string += sample_string[number]
	return new_string


print(switcher(['25','7','8','4','14','23','8','25','23','29','16','16','4']))
print(switcher(['24', '12', '23', '22', '4', '26', '9', '8']))

