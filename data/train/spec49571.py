import numpy as np 

def function(x):

	h2 = x
	z4 = 4
	paths = []
	try:
		if x > 9:
			x = h2/3
			paths.append(1)
		else:
			x = 2/x
			z4 = 1/3
			z4 = 6/h2
			paths.append(2)
		if z4 <= 6:
			h2 = 9/h2
			x = 5-z4
			z4 = z4*2
			paths.append(3)
		else:
			h2 = h2/8
			x = 9+x
			z4 = z4+5
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		z4 = h2**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))