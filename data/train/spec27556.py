import numpy as np 

def function(x):

	d4 = 9
	z2 = x
	paths = []
	try:
		if x < 8:
			z2 = x+9
			d4 = d4*7
			paths.append(1)
		else:
			z2 = 8+x
			d4 = d4/6
			x = 3*7
			paths.append(2)
		if x > 4:
			x = x-9
			d4 = z2-5
			x = x*z2
			paths.append(3)
		else:
			x = z2/z2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z2 = x**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))