import numpy as np 

def function(x):

	z8 = 0
	h9 = 9
	paths = []
	try:
		if h9 <= 1:
			z8 = z8*8
			z8 = z8-3
			h9 = 8+z8
			paths.append(1)
		else:
			z8 = x*9
			x = 9+x
			x = 0-x
			paths.append(2)
		if x > 2:
			h9 = 4+z8
			h9 = h9*1
			z8 = z8/x
			paths.append(3)
		else:
			z8 = x/h9
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		h9 = z8**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))