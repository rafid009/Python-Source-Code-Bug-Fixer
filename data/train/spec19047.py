import numpy as np 

def function(x):

	j0 = x
	z9 = x
	paths = []
	try:
		if j0 >= 7:
			x = 8/2
			z9 = 0*8
			z9 = x-4
			paths.append(1)
		else:
			j0 = j0+7
			x = 8/x
			z9 = z9*9
			paths.append(2)
		if z9 < 2:
			j0 = x/6
			paths.append(3)
		else:
			x = j0-4
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		x = j0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))