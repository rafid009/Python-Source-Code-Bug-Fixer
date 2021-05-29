import numpy as np 

def function(x):

	x6 = x
	z9 = 8
	paths = []
	try:
		if x6 <= 6:
			z9 = z9-z9
			x6 = x6*5
			paths.append(1)
		else:
			z9 = 5+z9
			x = x+x6
			paths.append(2)
		if x <= 0:
			x6 = x6-9
			x = 4/x
			paths.append(3)
		else:
			x = z9*x
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