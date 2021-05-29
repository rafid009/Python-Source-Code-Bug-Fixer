import numpy as np 

def function(x):

	x1 = 5
	h7 = x
	paths = []
	try:
		if x1 >= 5:
			x1 = 1*x1
			x = x+h7
			paths.append(1)
		else:
			x = h7*h7
			x1 = 8-x1
			paths.append(2)
		if h7 >= 8:
			h7 = h7-x1
			x1 = x/x
			paths.append(3)
		else:
			h7 = 6/h7
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