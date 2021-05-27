import numpy as np 

def function(x):

	i0 = x
	v4 = 1
	paths = []
	try:
		if v4 >= 1:
			v4 = v4/5
			paths.append(1)
		else:
			i0 = 0-i0
			paths.append(2)
		if x < 0:
			v4 = 8/v4
			v4 = 9*v4
			paths.append(3)
		else:
			i0 = i0+v4
			v4 = v4/v4
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