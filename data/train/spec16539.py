import numpy as np 

def function(x):

	k7 = x
	z8 = x
	paths = []
	try:
		if x >= 5:
			x = z8+k7
			paths.append(1)
		else:
			k7 = x-9
			k7 = 2*k7
			x = x+x
			paths.append(2)
		if x > 5:
			x = 9+x
			z8 = z8-9
			paths.append(3)
		else:
			z8 = 5+k7
			z8 = 9*z8
			x = x*0
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		x = k7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))