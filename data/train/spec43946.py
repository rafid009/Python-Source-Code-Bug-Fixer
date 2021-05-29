import numpy as np 

def function(x):

	v9 = x
	z5 = x
	paths = []
	try:
		if x >= 4:
			x = 2/x
			x = 4-z5
			z5 = z5/9
			paths.append(1)
		else:
			z5 = 2+z5
			paths.append(2)
		if x > 5:
			x = 9*x
			x = 2/x
			v9 = z5+v9
			paths.append(3)
		else:
			z5 = z5*2
			x = x/z5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v9 = x**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))