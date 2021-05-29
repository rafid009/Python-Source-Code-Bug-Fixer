import numpy as np 

def function(x):

	r3 = 8
	z9 = x
	paths = []
	try:
		if z9 < 7:
			z9 = z9-8
			r3 = r3/2
			x = 7/x
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if x >= 6:
			x = x*z9
			paths.append(3)
		else:
			x = z9-6
			r3 = z9*2
			r3 = r3-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))