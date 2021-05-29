import numpy as np 

def function(x):

	a7 = x
	z2 = x
	paths = []
	try:
		if x <= 4:
			z2 = z2+z2
			a7 = a7*z2
			paths.append(1)
		else:
			z2 = a7*2
			paths.append(2)
		if a7 > 6:
			a7 = 8/a7
			x = x-0
			paths.append(3)
		else:
			z2 = z2+z2
			z2 = z2+a7
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		a7 = z2**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))