import numpy as np 

def function(x):

	z9 = x
	i9 = 1
	paths = []
	try:
		if z9 > 0:
			x = 1*4
			z9 = x-1
			paths.append(1)
		else:
			x = x*x
			i9 = i9*x
			paths.append(2)
		if x > 3:
			z9 = z9*4
			z9 = z9*4
			x = x-7
			paths.append(3)
		else:
			z9 = z9+z9
			z9 = x+4
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		i9 = z9**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))