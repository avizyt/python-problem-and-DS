 


def smart_div(func):
	def inner(a, b):
		print("divide ", a ,"and ", b)
		if b == 0:
			print("Error!")
			return
		return func(a, b)
	return inner


@smart_div
def divide(a, b):
	return a/b 


print(divide(2, 0))