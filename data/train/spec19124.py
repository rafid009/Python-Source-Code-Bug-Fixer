import numpy as np 

def function(x):

	v1 = 5
	z8 = 4
	paths = []
	try:
		if x <= 4:
			z8 = x-8
			z8 = 6/7
			paths.append(1)
		else:
			x = 9-v1
			x = 7*9
			paths.append(2)
		if v1 >= 4:
			z8 = 2*z8
			x = x*5
			paths.append(3)
		else:
			v1 = 8+8
			v1 = x-v1
			v1 = z8*v1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))