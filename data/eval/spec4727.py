import numpy as np 

def function(x):

	h9 = 3
	a2 = 4
	paths = []
	try:
		if x >= 8:
			h9 = 9-h9
			paths.append(1)
		else:
			h9 = h9-1
			a2 = 2-a2
			h9 = 5*x
			paths.append(2)
		if x >= 2:
			h9 = h9/3
			paths.append(3)
		else:
			x = x/2
			h9 = a2-a2
			a2 = a2*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h9 = x**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))