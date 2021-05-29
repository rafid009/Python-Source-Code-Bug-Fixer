import numpy as np 

def function(x):

	b2 = x
	z9 = x
	paths = []
	try:
		if b2 > 7:
			b2 = b2+z9
			paths.append(1)
		else:
			x = 3-0
			z9 = x-x
			paths.append(2)
		if x > 0:
			x = b2-x
			z9 = 1+z9
			paths.append(3)
		else:
			b2 = 5*z9
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