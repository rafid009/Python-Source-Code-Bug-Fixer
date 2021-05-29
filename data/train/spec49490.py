import numpy as np 

def function(x):

	z1 = x
	d2 = x
	paths = []
	try:
		if d2 >= 1:
			x = 4*8
			d2 = z1*7
			x = 0+x
			paths.append(1)
		else:
			x = x*9
			z1 = 5+d2
			paths.append(2)
		if x >= 5:
			d2 = 1/d2
			x = x/x
			d2 = x*6
			paths.append(3)
		else:
			x = 9*z1
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		z1 = d2**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))