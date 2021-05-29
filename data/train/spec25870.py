import numpy as np 

def function(x):

	z2 = 5
	e8 = 3
	paths = []
	try:
		if x < 2:
			z2 = z2+7
			z2 = 8+z2
			paths.append(1)
		else:
			x = 1+x
			paths.append(2)
		if e8 < 0:
			e8 = e8/3
			z2 = z2*z2
			x = 4*1
			paths.append(3)
		else:
			e8 = 2/1
			e8 = e8/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))