import numpy as np 

def function(x):

	z1 = x
	d4 = x
	paths = []
	try:
		if x <= 4:
			d4 = 5*d4
			d4 = d4/d4
			paths.append(1)
		else:
			d4 = 6-z1
			z1 = x*9
			paths.append(2)
		if x > 7:
			z1 = 5-z1
			paths.append(3)
		else:
			x = x+9
			z1 = 7*z1
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