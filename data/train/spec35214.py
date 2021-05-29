import numpy as np 

def function(x):

	z4 = 2
	h6 = x
	paths = []
	try:
		if x > 5:
			x = 2-x
			h6 = 7/x
			z4 = h6+7
			paths.append(1)
		else:
			z4 = z4-z4
			x = x-9
			x = h6/x
			paths.append(2)
		if z4 < 6:
			x = h6/x
			z4 = 8*z4
			x = 7-8
			paths.append(3)
		else:
			z4 = 5-z4
			z4 = x*1
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		z4 = h6**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))