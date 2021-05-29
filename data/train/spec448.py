import numpy as np 

def function(x):

	i0 = x
	z2 = 5
	paths = []
	try:
		if i0 < 4:
			i0 = 5+i0
			paths.append(1)
		else:
			z2 = i0-z2
			z2 = z2+z2
			paths.append(2)
		if z2 >= 0:
			x = 5/9
			paths.append(3)
		else:
			i0 = 6/x
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		i0 = i0**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))