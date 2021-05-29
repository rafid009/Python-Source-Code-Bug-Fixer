import numpy as np 

def function(x):

	t0 = 1
	z6 = 2
	paths = []
	try:
		if z6 <= 8:
			x = x/7
			x = t0-9
			paths.append(1)
		else:
			x = x+5
			x = x*z6
			paths.append(2)
		if z6 > 7:
			z6 = x-z6
			x = t0*2
			paths.append(3)
		else:
			t0 = 3*x
			t0 = 2/t0
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