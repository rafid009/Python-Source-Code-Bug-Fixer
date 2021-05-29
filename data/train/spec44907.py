import numpy as np 

def function(x):

	z0 = x
	v5 = x
	paths = []
	try:
		if x > 9:
			z0 = z0+9
			x = x*7
			z0 = z0*1
			paths.append(1)
		else:
			z0 = z0/9
			v5 = v5-2
			v5 = 3*v5
			paths.append(2)
		if v5 < 2:
			z0 = 9*z0
			paths.append(3)
		else:
			x = 0*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))