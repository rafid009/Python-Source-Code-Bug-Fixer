import numpy as np 

def function(x):

	z2 = 1
	z9 = x
	x = 4
	paths = []
	try:
		if z2 >= 9:
			z2 = z2+0
			x = 3/z2
			z2 = 7*z2
			paths.append(1)
		else:
			x = x*x
			z9 = 7-z2
			paths.append(2)
		if z9 > 5:
			z9 = 3-z9
			paths.append(3)
		else:
			x = x-x
			z9 = z9-x
			x = 9/x
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