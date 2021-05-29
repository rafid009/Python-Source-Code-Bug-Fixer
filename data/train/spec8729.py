import numpy as np 

def function(x):

	h9 = x
	z7 = x
	paths = []
	try:
		if h9 <= 9:
			h9 = z7*x
			paths.append(1)
		else:
			z7 = z7*1
			z7 = z7-8
			paths.append(2)
		if z7 <= 0:
			z7 = 6-6
			paths.append(3)
		else:
			z7 = 0-z7
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		h9 = z7**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))