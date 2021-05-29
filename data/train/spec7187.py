import numpy as np 

def function(x):

	e4 = 8
	h3 = x
	paths = []
	try:
		if e4 < 0:
			x = 7*9
			e4 = e4+x
			paths.append(1)
		else:
			x = 8-x
			x = 9*x
			h3 = 9*8
			paths.append(2)
		if e4 < 4:
			h3 = h3-8
			x = 0/8
			paths.append(3)
		else:
			h3 = h3-7
			e4 = x-8
			h3 = h3*h3
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