import numpy as np 

def function(x):

	i0 = x
	i4 = x
	x = x
	paths = []
	try:
		if i4 > 8:
			i4 = i4-x
			paths.append(1)
		else:
			i0 = 9/i4
			paths.append(2)
		if i4 > 1:
			i0 = 5+i0
			paths.append(3)
		else:
			i0 = 9+i0
			i0 = x*6
			i0 = i4-8
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		x = i4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))