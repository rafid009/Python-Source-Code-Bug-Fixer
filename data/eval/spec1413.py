import numpy as np 

def function(x):

	h1 = x
	x4 = 2
	x = x
	paths = []
	try:
		if x4 <= 8:
			x = 3-x
			x4 = 8-2
			paths.append(1)
		else:
			h1 = h1*6
			x = x*h1
			h1 = h1+1
			paths.append(2)
		if x <= 4:
			h1 = 6+8
			paths.append(3)
		else:
			h1 = 5+h1
			x4 = x4*6
			x4 = 9/2
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