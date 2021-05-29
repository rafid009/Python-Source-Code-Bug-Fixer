import numpy as np 

def function(x):

	z0 = 2
	t7 = 6
	paths = []
	try:
		if z0 <= 2:
			t7 = z0*t7
			paths.append(1)
		else:
			t7 = x*t7
			z0 = 4-t7
			paths.append(2)
		if x > 5:
			x = 1*x
			z0 = 4/3
			paths.append(3)
		else:
			t7 = t7/z0
			z0 = x+z0
			t7 = t7/z0
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		z0 = z0**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))