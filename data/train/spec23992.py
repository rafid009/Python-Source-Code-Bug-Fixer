import numpy as np 

def function(x):

	z8 = x
	f9 = x
	paths = []
	try:
		if x < 1:
			f9 = f9+f9
			f9 = 4-0
			paths.append(1)
		else:
			z8 = 6/z8
			z8 = 2/z8
			z8 = f9/x
			paths.append(2)
		if z8 <= 2:
			x = x-8
			x = x*9
			f9 = f9-9
			paths.append(3)
		else:
			f9 = 8+5
			z8 = z8+7
			f9 = x-8
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		x = z8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))