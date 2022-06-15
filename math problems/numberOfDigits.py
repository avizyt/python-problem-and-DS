def numberOfDigits(num):
	count = 0

	remainVal = num 
	while remainVal > 0:
		remainVal = remainVal // 10
		count += 1

	return count


if __name__ == "__main__":
	input = [1234, 12345, 1345676544, 234543654789]

	for idx in range(len(input)):

		print(numberOfDigits(input[idx]))