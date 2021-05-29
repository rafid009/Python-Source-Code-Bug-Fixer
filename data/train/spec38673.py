import numpy as np 

def function(x):

	z4 = 4
	a7 = x
	paths = []
	try:
		if a7 >= 6:
			a7 = a7*z4
			paths.append(1)
		else:
			z4 = z4-5
			paths.append(2)
		if x > 9:
			z4 = z4*a7
			paths.append(3)
		else:
			z4 = z4-a7
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		a7 = z4**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))