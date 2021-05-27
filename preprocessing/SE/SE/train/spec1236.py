import numpy as np 

def function(x):

	e7 = 4
	z4 = 6
	paths = []
	try:
		if x > 7:
			x = 0*4
			x = x+z4
			paths.append(1)
		else:
			z4 = 2*5
			z4 = x*z4
			paths.append(2)
		if z4 <= 0:
			e7 = e7+4
			e7 = z4*9
			paths.append(3)
		else:
			x = 2-x
			e7 = z4/z4
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		x = z4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))