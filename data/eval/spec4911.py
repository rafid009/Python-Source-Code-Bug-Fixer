import numpy as np 

def function(x):

	h9 = 3
	e1 = 4
	paths = []
	try:
		if x < 9:
			h9 = h9-5
			e1 = e1/e1
			paths.append(1)
		else:
			h9 = 0-7
			paths.append(2)
		if x > 5:
			x = x+1
			paths.append(3)
		else:
			e1 = 9*e1
			x = x-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e1 = x**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))