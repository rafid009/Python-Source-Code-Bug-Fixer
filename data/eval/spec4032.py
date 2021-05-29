import numpy as np 

def function(x):

	b8 = 8
	z2 = 2
	paths = []
	try:
		if b8 >= 7:
			x = z2-4
			paths.append(1)
		else:
			z2 = x-4
			paths.append(2)
		if x > 3:
			z2 = 3*b8
			z2 = b8+1
			z2 = 2/z2
			paths.append(3)
		else:
			z2 = z2/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))