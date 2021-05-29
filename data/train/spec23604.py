import numpy as np 

def function(x):

	z2 = x
	e0 = 0
	x = 1
	paths = []
	try:
		if z2 < 2:
			e0 = 3*e0
			paths.append(1)
		else:
			z2 = z2+z2
			x = x-7
			x = 6/5
			paths.append(2)
		if e0 > 7:
			z2 = 3+z2
			x = x+5
			paths.append(3)
		else:
			e0 = e0+0
			x = x+9
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		z2 = z2**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))