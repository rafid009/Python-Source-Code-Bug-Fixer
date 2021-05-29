import numpy as np 

def function(x):

	z4 = 1
	t0 = x
	x = x
	paths = []
	try:
		if t0 > 6:
			z4 = 6+z4
			paths.append(1)
		else:
			t0 = x/t0
			paths.append(2)
		if x > 9:
			x = t0-x
			t0 = 7/t0
			x = 6*t0
			paths.append(3)
		else:
			t0 = 5/t0
			x = x*5
			z4 = x+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))