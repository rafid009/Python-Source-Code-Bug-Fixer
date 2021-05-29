import numpy as np 

def function(x):

	e0 = x
	h4 = x
	paths = []
	try:
		if e0 <= 9:
			h4 = 8-6
			paths.append(1)
		else:
			h4 = 0+4
			e0 = e0-0
			paths.append(2)
		if e0 >= 2:
			e0 = 6*h4
			x = 5*x
			e0 = x+4
			paths.append(3)
		else:
			h4 = 6/7
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		h4 = e0**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))