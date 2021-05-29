import numpy as np 

def function(x):

	w5 = x
	z6 = 8
	paths = []
	try:
		if w5 > 2:
			x = x-w5
			x = x*9
			paths.append(1)
		else:
			z6 = z6+0
			x = 4/x
			paths.append(2)
		if x <= 4:
			x = x-1
			z6 = z6+z6
			paths.append(3)
		else:
			x = 1-x
			z6 = 7*z6
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