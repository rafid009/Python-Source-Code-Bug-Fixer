import numpy as np 

def function(x):

	z5 = x
	h3 = x
	x = 4
	paths = []
	try:
		if h3 >= 4:
			z5 = h3*z5
			paths.append(1)
		else:
			x = 0-x
			paths.append(2)
		if z5 < 6:
			z5 = z5+6
			h3 = z5*1
			paths.append(3)
		else:
			h3 = 7+h3
			h3 = 5/6
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		h3 = z5**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))