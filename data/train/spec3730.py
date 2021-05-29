import numpy as np 

def function(x):

	i5 = x
	z1 = 3
	paths = []
	try:
		if x >= 5:
			x = 5+7
			x = i5*9
			z1 = 5-z1
			paths.append(1)
		else:
			i5 = z1/i5
			z1 = x-2
			z1 = z1-3
			paths.append(2)
		if z1 < 5:
			i5 = 6+i5
			i5 = i5+7
			z1 = z1+z1
			paths.append(3)
		else:
			i5 = i5-z1
			z1 = x*2
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