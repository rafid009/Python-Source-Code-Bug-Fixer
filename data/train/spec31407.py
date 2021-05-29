import numpy as np 

def function(x):

	z4 = 7
	h3 = x
	paths = []
	try:
		if h3 <= 5:
			x = h3-3
			h3 = 0*x
			z4 = z4/6
			paths.append(1)
		else:
			x = 6+x
			x = x+x
			x = 6/h3
			paths.append(2)
		if x > 3:
			x = h3*5
			x = h3+x
			x = 8+x
			paths.append(3)
		else:
			x = h3-4
			h3 = z4+h3
			z4 = 3/z4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h3 = x**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))