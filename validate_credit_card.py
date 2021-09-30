def validate(n):
	new_d = [x for x in str(n)]
	validated = []
	final = []
	outcome = 0
	if len(new_d) % 2 == 0:
		for d in new_d:
			if new_d.index(d) % 2 == 0:
				validated.append(int(d) * 2)
			else:
				validated.append(int(d))

	else:
		for d in new_d:
			if new_d.index(d) % 2 != 0:
				validated.append(int(d) * 2)
			else:
				validated.append(int(d))

	for n in validated:
		if n > 9:
			final.append(n - 9)
		else:
			final.append(n)

	for n in final:
		outcome += n 
		print(outcome)

	if outcome % 10 == 0:

		return True
	else:
		return False

print(validate(891))

