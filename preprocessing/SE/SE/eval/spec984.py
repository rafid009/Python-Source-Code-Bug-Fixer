import numpy as np 

def function(x):

	h3 = 4
	z4 = 7
	paths = []
	try:
		if x > 6:
			x = x/8
			h3 = h3-8
			x = 3+x
			paths.append(1)
		else:
			x = 5/7
			h3 = h3+x
			x = z4*x
			paths.append(2)
		if h3 >= 7:
			z4 = 4+6
			paths.append(3)
		else:
			z4 = z4*7
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		z4 = h3**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))