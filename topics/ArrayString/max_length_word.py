def maxWord(sen):
	alpha = "abcdefghijklmnopqrstuvwxyz"
	letters = list(alpha)

	words = sen.split()

	max_len = 0
	max_word = 0 
	for w in range(len(words))  :
		c = 0
		for l in words[w]:
			if l in letters:
				c += 1
		if c > max_len:
			max_len = c 
			max_word = words[w]

	return max_word


if __name__ == "__main__":
	input = "the time$%% of flight is not known to us"
	print(maxWord(input))