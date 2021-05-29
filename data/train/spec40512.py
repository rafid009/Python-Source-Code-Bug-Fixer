import numpy as np 

def function(x):

	o0 = 7
	z1 = 5
	paths = []
	try:
		if x <= 3:
			o0 = o0+0
			x = 9*x
			paths.append(1)
		else:
			o0 = o0-5
			z1 = x*x
			o0 = o0-8
			paths.append(2)
		if x >= 0:
			x = x-z1
			o0 = x+6
			o0 = 4-0
			paths.append(3)
		else:
			x = 0/x
			z1 = z1-2
			z1 = o0*z1
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