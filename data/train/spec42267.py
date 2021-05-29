import numpy as np 

def function(x):

	z4 = x
	l0 = x
	paths = []
	try:
		if x > 9:
			x = 4+9
			paths.append(1)
		else:
			z4 = z4-8
			x = x*2
			x = z4-x
			paths.append(2)
		if x < 4:
			z4 = l0*z4
			l0 = 4*l0
			x = x+x
			paths.append(3)
		else:
			z4 = x*l0
			l0 = 6/l0
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