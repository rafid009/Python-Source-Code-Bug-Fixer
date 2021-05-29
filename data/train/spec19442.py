import numpy as np 

def function(x):

	h7 = x
	h2 = 3
	paths = []
	try:
		if h7 <= 0:
			x = x+4
			paths.append(1)
		else:
			h7 = 5+h7
			paths.append(2)
		if x > 1:
			h2 = h7*x
			paths.append(3)
		else:
			h7 = h7-5
			h7 = 0+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))