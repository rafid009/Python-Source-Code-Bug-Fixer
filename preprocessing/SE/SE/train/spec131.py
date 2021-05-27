import numpy as np 

def function(x):

	z4 = x
	a2 = x
	paths = []
	try:
		if a2 <= 4:
			x = x-4
			a2 = 6/a2
			paths.append(1)
		else:
			z4 = 0/z4
			paths.append(2)
		if a2 > 0:
			z4 = z4*5
			paths.append(3)
		else:
			x = 9*x
			x = z4-4
			z4 = z4+x
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))