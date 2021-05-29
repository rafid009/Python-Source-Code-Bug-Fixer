import numpy as np 

def function(x):

	r4 = 3
	z6 = 8
	paths = []
	try:
		if x <= 3:
			z6 = z6/9
			paths.append(1)
		else:
			x = x*z6
			x = 9+z6
			paths.append(2)
		if z6 < 7:
			x = x+1
			z6 = x-0
			paths.append(3)
		else:
			x = z6*8
			z6 = z6-8
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