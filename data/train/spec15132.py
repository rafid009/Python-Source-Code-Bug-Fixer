import numpy as np 

def function(x):

	h4 = x
	a3 = 2
	paths = []
	try:
		if x <= 9:
			a3 = a3+h4
			a3 = a3*6
			h4 = h4+h4
			paths.append(1)
		else:
			a3 = a3+4
			h4 = h4-h4
			paths.append(2)
		if h4 >= 0:
			x = x-a3
			paths.append(3)
		else:
			a3 = a3/h4
			h4 = h4+3
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