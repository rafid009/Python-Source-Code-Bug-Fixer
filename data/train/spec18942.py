import numpy as np 

def function(x):

	i0 = x
	x4 = x
	paths = []
	try:
		if x >= 2:
			x = 7-x
			paths.append(1)
		else:
			i0 = i0+2
			i0 = i0+2
			paths.append(2)
		if i0 >= 8:
			x4 = i0+1
			x = x4+4
			paths.append(3)
		else:
			x = 9*x4
			i0 = 6/i0
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		x = i0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))