import numpy as np 

def function(x):

	h2 = 1
	a8 = x
	paths = []
	try:
		if x > 0:
			h2 = h2-6
			paths.append(1)
		else:
			h2 = 6/8
			paths.append(2)
		if a8 < 2:
			h2 = h2-a8
			paths.append(3)
		else:
			a8 = 1+3
			a8 = a8-7
			x = x/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h2 = x**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))