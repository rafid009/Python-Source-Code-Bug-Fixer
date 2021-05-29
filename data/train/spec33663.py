import numpy as np 

def function(x):

	z1 = x
	d4 = x
	paths = []
	try:
		if z1 <= 5:
			d4 = d4+d4
			paths.append(1)
		else:
			x = 2*d4
			d4 = 8*z1
			d4 = d4/5
			paths.append(2)
		if x <= 6:
			d4 = d4/6
			z1 = z1+d4
			paths.append(3)
		else:
			x = 9*2
			x = x*x
			z1 = z1+6
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		z1 = d4**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))