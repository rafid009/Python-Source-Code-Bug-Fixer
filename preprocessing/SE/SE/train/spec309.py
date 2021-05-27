import numpy as np 

def function(x):

	z9 = x
	t6 = x
	paths = []
	try:
		if t6 >= 0:
			x = 9-x
			z9 = z9*2
			t6 = 6-z9
			paths.append(1)
		else:
			x = x/5
			x = t6/x
			paths.append(2)
		if z9 < 1:
			z9 = z9-x
			paths.append(3)
		else:
			x = x-2
			x = z9/x
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