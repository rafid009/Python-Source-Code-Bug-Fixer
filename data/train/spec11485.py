import numpy as np 

def function(x):

	x2 = x
	z4 = x
	paths = []
	try:
		if x > 9:
			x = x*5
			x = 0/3
			paths.append(1)
		else:
			x = x/3
			z4 = z4*z4
			x = x+9
			paths.append(2)
		if x < 8:
			z4 = z4+3
			z4 = z4/z4
			z4 = z4/4
			paths.append(3)
		else:
			x2 = x2-2
			z4 = 4/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))