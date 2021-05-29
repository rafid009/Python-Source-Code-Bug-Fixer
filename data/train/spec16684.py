import numpy as np 

def function(x):

	h1 = x
	z6 = x
	x = x
	paths = []
	try:
		if h1 < 6:
			h1 = h1*9
			h1 = h1-h1
			h1 = z6/4
			paths.append(1)
		else:
			h1 = z6*h1
			h1 = 3-h1
			x = x-z6
			paths.append(2)
		if z6 >= 7:
			x = z6/1
			h1 = h1*8
			z6 = z6*5
			paths.append(3)
		else:
			x = 9-x
			x = x+h1
			h1 = h1*3
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