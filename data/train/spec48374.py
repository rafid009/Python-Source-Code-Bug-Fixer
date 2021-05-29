import numpy as np 

def function(x):

	v4 = 8
	n0 = x
	paths = []
	try:
		if v4 > 0:
			v4 = 4/v4
			v4 = 9-v4
			v4 = x+v4
			paths.append(1)
		else:
			x = x+4
			n0 = x-n0
			n0 = x-n0
			paths.append(2)
		if x > 1:
			n0 = n0-x
			paths.append(3)
		else:
			v4 = 4-v4
			v4 = v4/n0
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		v4 = v4**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))