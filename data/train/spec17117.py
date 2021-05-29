import numpy as np 

def function(x):

	t2 = 5
	z6 = 0
	paths = []
	try:
		if x > 9:
			x = x*x
			paths.append(1)
		else:
			z6 = 1+z6
			t2 = t2/x
			z6 = z6*1
			paths.append(2)
		if z6 > 6:
			z6 = 2-2
			x = 0*1
			t2 = t2-8
			paths.append(3)
		else:
			x = x+2
			t2 = 1-t2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))