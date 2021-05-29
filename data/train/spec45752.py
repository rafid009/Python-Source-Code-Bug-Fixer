import numpy as np 

def function(x):

	z9 = 0
	k7 = 8
	paths = []
	try:
		if x >= 0:
			x = 5-z9
			k7 = k7/1
			z9 = z9+x
			paths.append(1)
		else:
			x = 1*x
			k7 = 5-1
			paths.append(2)
		if z9 >= 5:
			z9 = 4/z9
			z9 = z9*k7
			z9 = x/k7
			paths.append(3)
		else:
			k7 = x*k7
			z9 = x+z9
			z9 = z9+9
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		z9 = z9**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))