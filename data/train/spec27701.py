import numpy as np 

def function(x):

	i2 = x
	z9 = 3
	paths = []
	try:
		if x <= 7:
			z9 = z9/6
			x = 2/x
			x = 7-9
			paths.append(1)
		else:
			x = x*1
			z9 = 4/x
			paths.append(2)
		if i2 <= 1:
			z9 = 3-6
			i2 = 8+4
			paths.append(3)
		else:
			z9 = 6*9
			z9 = z9+z9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))