import numpy as np 

def function(x):

	z9 = 0
	b6 = 9
	x = x
	paths = []
	try:
		if z9 >= 8:
			z9 = x/7
			z9 = b6-b6
			paths.append(1)
		else:
			x = x-b6
			paths.append(2)
		if z9 >= 4:
			b6 = 9-b6
			paths.append(3)
		else:
			b6 = b6*9
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