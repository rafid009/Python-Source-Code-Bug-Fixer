import numpy as np 

def function(x):

	l6 = x
	h6 = x
	paths = []
	try:
		if l6 > 1:
			l6 = l6-2
			paths.append(1)
		else:
			h6 = x-h6
			paths.append(2)
		if l6 > 2:
			l6 = l6-9
			x = 4*x
			paths.append(3)
		else:
			h6 = 9/7
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