import numpy as np 

def function(x):

	k7 = x
	z9 = 7
	x = 0
	paths = []
	try:
		if z9 >= 2:
			x = k7*x
			z9 = 1/k7
			x = x-6
			paths.append(1)
		else:
			k7 = 8/k7
			k7 = k7*5
			paths.append(2)
		if x > 2:
			k7 = k7+9
			k7 = k7+7
			z9 = z9*x
			paths.append(3)
		else:
			z9 = z9+0
			z9 = 3*8
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