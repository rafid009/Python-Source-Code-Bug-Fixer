import numpy as np 

def function(x):

	z2 = x
	j1 = 7
	paths = []
	try:
		if z2 < 3:
			z2 = 4+x
			paths.append(1)
		else:
			j1 = z2-6
			paths.append(2)
		if z2 >= 6:
			x = x-x
			j1 = 1*j1
			paths.append(3)
		else:
			x = x/z2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j1 = x**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))