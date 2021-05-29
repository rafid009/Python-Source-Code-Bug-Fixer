import numpy as np 

def function(x):

	b3 = x
	z6 = 9
	paths = []
	try:
		if b3 > 8:
			x = 4-8
			z6 = x-8
			paths.append(1)
		else:
			b3 = 3*b3
			b3 = 7+0
			paths.append(2)
		if b3 <= 9:
			z6 = z6*b3
			z6 = b3+z6
			paths.append(3)
		else:
			x = 8-x
			b3 = 3-8
			z6 = z6-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))