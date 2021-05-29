import numpy as np 

def function(x):

	e8 = 0
	h2 = x
	paths = []
	try:
		if e8 >= 2:
			e8 = e8+7
			h2 = h2-2
			paths.append(1)
		else:
			h2 = 9-x
			e8 = e8-x
			paths.append(2)
		if e8 <= 2:
			x = x-x
			paths.append(3)
		else:
			h2 = x+h2
			e8 = 6/8
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