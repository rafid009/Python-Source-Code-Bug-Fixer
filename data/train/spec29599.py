import numpy as np 

def function(x):

	h7 = 0
	z6 = 2
	paths = []
	try:
		if h7 >= 6:
			z6 = z6-2
			h7 = h7/h7
			h7 = 8/3
			paths.append(1)
		else:
			z6 = z6+h7
			h7 = h7-4
			z6 = z6*1
			paths.append(2)
		if h7 <= 3:
			h7 = 6/4
			h7 = z6/h7
			z6 = z6-0
			paths.append(3)
		else:
			h7 = 9-h7
			h7 = 5+h7
			h7 = h7*3
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