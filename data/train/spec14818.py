import numpy as np 

def function(x):

	h6 = x
	z4 = x
	paths = []
	try:
		if x <= 4:
			x = x/7
			z4 = h6-z4
			paths.append(1)
		else:
			z4 = 8+z4
			paths.append(2)
		if h6 < 9:
			z4 = 5+z4
			z4 = z4-z4
			paths.append(3)
		else:
			h6 = x/h6
			x = h6*x
			h6 = 5-h6
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		x = h6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))