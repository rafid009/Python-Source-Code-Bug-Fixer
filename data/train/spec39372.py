import numpy as np 

def function(x):

	e4 = 1
	h3 = x
	paths = []
	try:
		if h3 > 8:
			e4 = x-5
			x = x*x
			h3 = h3*7
			paths.append(1)
		else:
			x = x/6
			e4 = 5+e4
			e4 = e4/6
			paths.append(2)
		if h3 >= 2:
			x = x*4
			paths.append(3)
		else:
			e4 = 7-e4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))