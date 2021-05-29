import numpy as np 

def function(x):

	z5 = 0
	i6 = 7
	paths = []
	try:
		if z5 <= 1:
			i6 = 9+8
			z5 = 4/x
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if i6 >= 5:
			z5 = z5-0
			paths.append(3)
		else:
			i6 = 9+i6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))