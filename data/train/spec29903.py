import numpy as np 

def function(x):

	t9 = 9
	z0 = 7
	paths = []
	try:
		if t9 <= 5:
			t9 = 7-t9
			z0 = t9*z0
			z0 = 5/z0
			paths.append(1)
		else:
			z0 = t9*t9
			z0 = 1/z0
			paths.append(2)
		if x < 2:
			z0 = z0+6
			paths.append(3)
		else:
			x = 0+7
			t9 = t9/7
			t9 = t9/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z0 = x**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))