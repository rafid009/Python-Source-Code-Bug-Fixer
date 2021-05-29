import numpy as np 

def function(x):

	z5 = 7
	i4 = 8
	paths = []
	try:
		if z5 >= 1:
			i4 = i4-i4
			paths.append(1)
		else:
			z5 = z5/5
			paths.append(2)
		if i4 > 1:
			z5 = 4+9
			x = x/x
			z5 = i4+z5
			paths.append(3)
		else:
			i4 = i4/3
			i4 = x+9
			i4 = 7/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))