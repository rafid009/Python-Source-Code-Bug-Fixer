import numpy as np 

def function(x):

	z0 = x
	i5 = x
	paths = []
	try:
		if i5 > 0:
			x = 7+x
			paths.append(1)
		else:
			i5 = i5+6
			z0 = z0-z0
			z0 = z0-4
			paths.append(2)
		if z0 <= 9:
			x = 3*x
			paths.append(3)
		else:
			i5 = i5/z0
			z0 = 7*8
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		i5 = i5**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))