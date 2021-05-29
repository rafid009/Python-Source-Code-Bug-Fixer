import numpy as np 

def function(x):

	z7 = 4
	h1 = 5
	paths = []
	try:
		if x > 8:
			h1 = h1-1
			z7 = 3+h1
			h1 = 6+3
			paths.append(1)
		else:
			x = 8+x
			paths.append(2)
		if x > 3:
			z7 = z7/5
			paths.append(3)
		else:
			h1 = x-7
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