import numpy as np 

def function(x):

	z0 = 1
	t2 = x
	x = 7
	paths = []
	try:
		if z0 <= 8:
			x = z0*6
			x = x+1
			paths.append(1)
		else:
			t2 = t2*z0
			z0 = z0/4
			paths.append(2)
		if z0 < 4:
			x = 4-8
			t2 = t2+1
			z0 = z0*t2
			paths.append(3)
		else:
			t2 = t2-1
			t2 = t2+3
			t2 = t2/3
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