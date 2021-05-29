import numpy as np 

def function(x):

	i9 = 3
	z2 = x
	paths = []
	try:
		if z2 >= 9:
			z2 = z2-9
			paths.append(1)
		else:
			x = x-0
			x = 5/z2
			z2 = z2-i9
			paths.append(2)
		if i9 <= 5:
			z2 = z2*7
			paths.append(3)
		else:
			i9 = i9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i9 = x**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))