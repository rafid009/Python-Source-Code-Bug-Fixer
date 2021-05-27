import numpy as np 

def function(x):

	b0 = 6
	z4 = 0
	paths = []
	try:
		if x < 2:
			z4 = z4+5
			b0 = b0+8
			b0 = z4-b0
			paths.append(1)
		else:
			x = x*z4
			b0 = z4-z4
			paths.append(2)
		if x < 4:
			b0 = 9-b0
			z4 = z4-b0
			b0 = 6-b0
			paths.append(3)
		else:
			b0 = b0+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b0 = x**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))