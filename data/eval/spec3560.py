import numpy as np 

def function(x):

	i7 = 6
	z9 = x
	paths = []
	try:
		if z9 > 1:
			z9 = z9*5
			paths.append(1)
		else:
			i7 = 2*z9
			x = 4*x
			paths.append(2)
		if i7 > 9:
			z9 = z9/2
			paths.append(3)
		else:
			i7 = 5-x
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		z9 = i7**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))