# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.


def descending_order(num):
	list1 = []
	for x in str(num):
		list1.append(x)
		list1.sort(reverse=True)
		a = "".join(list1)
	return a	
		

print(descending_order(14132412312))