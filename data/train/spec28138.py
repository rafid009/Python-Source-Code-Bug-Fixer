import numpy as np 

def function(x):

	k6 = 3
	i0 = 0
	paths = []
	try:
		if k6 >= 9:
			k6 = k6/3
			k6 = 9-i0
			paths.append(1)
		else:
			i0 = i0*8
			paths.append(2)
		if k6 > 1:
			k6 = k6-3
			paths.append(3)
		else:
			x = x/8
			i0 = 6/6
			x = 8-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))