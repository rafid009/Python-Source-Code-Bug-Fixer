import numpy as np 

def function(x):

	e5 = x
	h6 = x
	paths = []
	try:
		if h6 >= 2:
			x = 2+e5
			e5 = 6+6
			e5 = e5/4
			paths.append(1)
		else:
			h6 = h6+h6
			e5 = e5/5
			paths.append(2)
		if e5 >= 6:
			e5 = x/2
			h6 = 4*h6
			paths.append(3)
		else:
			h6 = h6/e5
			h6 = 1/1
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