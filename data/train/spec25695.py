import numpy as np 

def function(x):

	z3 = x
	h1 = 7
	paths = []
	try:
		if h1 <= 2:
			x = 9/z3
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if h1 <= 1:
			h1 = z3/h1
			paths.append(3)
		else:
			h1 = h1-2
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