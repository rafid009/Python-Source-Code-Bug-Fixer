import numpy as np 

def function(x):

	z6 = x
	z9 = 3
	x = x
	paths = []
	try:
		if x >= 0:
			x = x-8
			x = z6*x
			z6 = 2+z6
			paths.append(1)
		else:
			z9 = x/z6
			paths.append(2)
		if z9 < 8:
			z6 = z6-0
			z9 = 6/z9
			z6 = z6+z9
			paths.append(3)
		else:
			z6 = z6*1
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