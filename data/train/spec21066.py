import numpy as np 

def function(x):

	h1 = 0
	f9 = 7
	paths = []
	try:
		if f9 > 8:
			f9 = h1+4
			x = f9*x
			paths.append(1)
		else:
			f9 = f9*x
			h1 = 6/8
			x = 2*x
			paths.append(2)
		if h1 < 5:
			f9 = h1/5
			paths.append(3)
		else:
			h1 = 9+h1
			h1 = 7*h1
			x = x/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h1 = x**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))