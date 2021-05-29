import numpy as np 

def function(x):

	n0 = x
	u4 = 8
	paths = []
	try:
		if x < 2:
			n0 = n0-7
			paths.append(1)
		else:
			n0 = n0*n0
			u4 = 1/u4
			paths.append(2)
		if u4 >= 3:
			u4 = 3-u4
			paths.append(3)
		else:
			u4 = 5-4
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		n0 = u4**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))