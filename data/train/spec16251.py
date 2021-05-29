import numpy as np 

def function(x):

	z4 = x
	b2 = x
	paths = []
	try:
		if b2 <= 1:
			x = 7/x
			z4 = z4*2
			x = x/7
			paths.append(1)
		else:
			z4 = z4+0
			x = 4*x
			paths.append(2)
		if x >= 1:
			z4 = 0+z4
			z4 = b2*z4
			paths.append(3)
		else:
			b2 = b2/1
			x = 7*x
			z4 = z4/2
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