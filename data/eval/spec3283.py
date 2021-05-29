import numpy as np 

def function(x):

	z9 = x
	z6 = 0
	paths = []
	try:
		if z6 <= 7:
			z9 = z9/7
			x = 1-z9
			z6 = 8/6
			paths.append(1)
		else:
			z9 = x/z6
			z9 = 4*9
			x = 2/3
			paths.append(2)
		if z9 <= 2:
			z9 = z9+1
			z6 = z6/z9
			z9 = z9-9
			paths.append(3)
		else:
			x = z9-z6
			z9 = 8-z9
			z6 = z6/9
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		z9 = z6**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))