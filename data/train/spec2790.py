import numpy as np 

def function(x):

	z9 = x
	v7 = x
	paths = []
	try:
		if z9 <= 9:
			x = 6+x
			paths.append(1)
		else:
			z9 = x-0
			x = x*9
			x = 8*x
			paths.append(2)
		if z9 <= 0:
			x = x-z9
			z9 = z9+z9
			paths.append(3)
		else:
			z9 = 3-z9
			z9 = z9+z9
			v7 = v7+6
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		x = z9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))