import numpy as np 

def function(x):

	x1 = x
	z9 = 2
	paths = []
	try:
		if x1 > 9:
			x = x*6
			z9 = 0*z9
			paths.append(1)
		else:
			z9 = z9+6
			paths.append(2)
		if z9 >= 8:
			x1 = 1+x1
			x = x+x
			x1 = 2/x1
			paths.append(3)
		else:
			x = x/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x1 = x**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))