texts = "abcadghadcbnklrmtnelksdgasvn"

letters = list(texts)


from collections import Counter

letter_cnt = Counter(letters)
top_4 = letter_cnt.most_common(4)

print(top_4)