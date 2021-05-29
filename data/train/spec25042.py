import numpy as np 

def function(x):

	z4 = x
	r3 = 4
	x = x
	paths = []
	try:
		if z4 > 1:
			r3 = r3+r3
			z4 = r3-z4
			paths.append(1)
		else:
			z4 = 2+z4
			paths.append(2)
		if r3 <= 5:
			z4 = r3+z4
			r3 = 2+r3
			paths.append(3)
		else:
			z4 = 7*x
			r3 = 8+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))