import numpy as np 

def function(x):

	f5 = x
	z6 = 5
	paths = []
	try:
		if z6 >= 4:
			x = z6-f5
			paths.append(1)
		else:
			x = x*z6
			f5 = 3*f5
			paths.append(2)
		if x <= 9:
			x = 6*x
			paths.append(3)
		else:
			x = 0+f5
			z6 = z6/f5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))