import numpy as np 

def function(x):

	j8 = x
	z9 = x
	paths = []
	try:
		if j8 > 1:
			z9 = 0/3
			z9 = 2*z9
			z9 = j8-z9
			paths.append(1)
		else:
			j8 = 2-8
			paths.append(2)
		if x > 3:
			x = 6*9
			z9 = z9+3
			paths.append(3)
		else:
			x = j8/x
			z9 = 6-4
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