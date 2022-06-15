def findDivisor(num):
	divisor = []

	for i in range(num//2):
		if num // i == 0:
			divisor.append(i) 

	return divisor



if __name__ == "__main__":
	inputs = [25, 12, 8, 45]

	for i in range(len(inputs)):
		print(findDivisor(inputs[i]))