import numpy as np 

def function(x):

	i0 = 5
	z1 = x
	paths = []
	try:
		if z1 > 4:
			x = 6*8
			paths.append(1)
		else:
			x = 1*8
			i0 = i0-5
			x = x-3
			paths.append(2)
		if i0 > 1:
			x = 5/7
			x = x*1
			paths.append(3)
		else:
			i0 = i0-1
			x = 0-9
			z1 = 9/z1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))