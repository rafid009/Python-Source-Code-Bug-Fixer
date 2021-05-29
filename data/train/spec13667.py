import numpy as np 

def function(x):

	h1 = 5
	a0 = 5
	paths = []
	try:
		if a0 < 3:
			a0 = 3-a0
			paths.append(1)
		else:
			a0 = 7-x
			x = x*x
			paths.append(2)
		if a0 >= 7:
			a0 = a0*8
			x = x-7
			paths.append(3)
		else:
			h1 = 5+a0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h1 = x**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))