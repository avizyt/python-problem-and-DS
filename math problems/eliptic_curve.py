import numpy as np 
import matplotlib.pyplot as plt 

def eliptic(x,a,b):
	y_sqr = x**3 + a * x + b 
	return y_sqr

def sqrt_of_eliptic(y_sqr):
	return np.sqrt(y_sqr)


if __name__ == "__main__":

	a, b =  12, 32 
	x = np.arange(-100, 100)
	elps = [eliptic(i, a, b) for i in x ]
	print(elps)
	
	plt.plot(x, elps)
	plt.show()