import numpy as np 

def function(x):

	z4 = x
	p7 = x
	x = x
	paths = []
	try:
		if z4 >= 6:
			z4 = 6*z4
			paths.append(1)
		else:
			z4 = z4+2
			z4 = z4/5
			paths.append(2)
		if p7 > 0:
			p7 = 8-p7
			paths.append(3)
		else:
			p7 = 5-x
			x = 4/7
			p7 = p7/4
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		z4 = p7**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))