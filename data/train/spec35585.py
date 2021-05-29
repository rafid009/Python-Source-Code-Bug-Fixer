import numpy as np 

def function(x):

	z9 = 8
	i9 = 9
	paths = []
	try:
		if z9 <= 6:
			z9 = z9/x
			z9 = z9-9
			i9 = z9/z9
			paths.append(1)
		else:
			x = 6-i9
			z9 = z9-9
			x = x-z9
			paths.append(2)
		if i9 >= 0:
			x = x+x
			paths.append(3)
		else:
			z9 = 9+1
			i9 = 2*4
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