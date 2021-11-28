def dig_pow(n, p):

	test_list = [int(i) for i in str(n)]
	print(test_list)
	final_number = []

	for i in test_list:
		final_number.append(i ** p)
		print(final_number)
		p += 1
		
	test_number = sum(final_number) / n
	print(test_number)
	if sum(final_number) / test_number == n:
		return int(test_number)
	else:
		return -1

print(dig_pow(92, 1))