import numpy as np 

def function(x):

	j8 = 8
	z5 = 3
	x = x
	paths = []
	try:
		if j8 <= 8:
			j8 = j8*4
			z5 = z5-2
			paths.append(1)
		else:
			z5 = 7*x
			x = 9/x
			x = x*z5
			paths.append(2)
		if j8 <= 0:
			z5 = j8/z5
			z5 = z5-z5
			paths.append(3)
		else:
			z5 = z5+0
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