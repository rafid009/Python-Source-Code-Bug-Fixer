import numpy as np 

def function(x):

	r5 = 7
	z2 = x
	paths = []
	try:
		if r5 < 8:
			x = x-6
			z2 = 2-x
			z2 = 1*z2
			paths.append(1)
		else:
			z2 = 0-z2
			r5 = 1+r5
			paths.append(2)
		if x >= 8:
			r5 = r5+r5
			r5 = 7+9
			x = x/1
			paths.append(3)
		else:
			r5 = 4/3
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