import numpy as np 

def function(x):

	z2 = x
	v8 = x
	paths = []
	try:
		if z2 > 3:
			z2 = 3*9
			v8 = v8/v8
			z2 = z2+5
			paths.append(1)
		else:
			x = 5*x
			paths.append(2)
		if z2 > 0:
			v8 = 6+4
			z2 = z2*8
			x = x-2
			paths.append(3)
		else:
			z2 = z2-1
			x = v8+x
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