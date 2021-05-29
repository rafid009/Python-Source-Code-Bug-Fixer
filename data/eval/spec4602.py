import numpy as np 

def function(x):

	z2 = x
	i0 = x
	paths = []
	try:
		if z2 <= 9:
			z2 = i0/1
			paths.append(1)
		else:
			x = i0/x
			x = x/x
			x = x-6
			paths.append(2)
		if i0 <= 7:
			x = x-x
			paths.append(3)
		else:
			x = i0-4
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		i0 = z2**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))