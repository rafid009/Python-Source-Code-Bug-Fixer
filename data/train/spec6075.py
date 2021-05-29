import numpy as np 

def function(x):

	z9 = 9
	k4 = x
	paths = []
	try:
		if k4 > 7:
			k4 = z9+k4
			paths.append(1)
		else:
			x = x-2
			k4 = k4+5
			x = k4*9
			paths.append(2)
		if z9 < 5:
			z9 = x+z9
			z9 = z9-9
			z9 = 2-4
			paths.append(3)
		else:
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))