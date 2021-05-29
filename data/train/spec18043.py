import numpy as np 

def function(x):

	i0 = x
	v3 = 0
	paths = []
	try:
		if i0 < 9:
			x = v3*1
			paths.append(1)
		else:
			x = 7-9
			i0 = i0-2
			x = x*3
			paths.append(2)
		if i0 < 5:
			x = 9-3
			paths.append(3)
		else:
			v3 = 3-x
			x = 1+3
			i0 = i0*1
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