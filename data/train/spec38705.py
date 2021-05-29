import numpy as np 

def function(x):

	z0 = 0
	t0 = x
	paths = []
	try:
		if z0 <= 3:
			t0 = t0/3
			z0 = 7/5
			paths.append(1)
		else:
			z0 = 5/z0
			z0 = z0+2
			paths.append(2)
		if x <= 9:
			t0 = t0+2
			paths.append(3)
		else:
			t0 = t0-t0
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		z0 = t0**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))