def make_pretty(func):
	def inner():
	  print("I got decorated!")
	  func()
	return inner

@make_pretty
def ordinary():
	print("I am ordinary") 


if __name__ == "__main__":
	x = 12
	y = 3
	ordinary()
