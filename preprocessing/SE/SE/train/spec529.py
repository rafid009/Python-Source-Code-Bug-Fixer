import numpy as np 

def function(x):

	e3 = 5
	h3 = x
	paths = []
	try:
		if h3 > 3:
			x = x+8
			paths.append(1)
		else:
			e3 = 6*e3
			e3 = 0/3
			e3 = e3+e3
			paths.append(2)
		if e3 >= 8:
			h3 = h3/2
			x = x-0
			paths.append(3)
		else:
			h3 = 0/h3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))