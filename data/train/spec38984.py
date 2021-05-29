import numpy as np 

def function(x):

	u2 = x
	x4 = 1
	paths = []
	try:
		if x >= 0:
			x = x4/x
			paths.append(1)
		else:
			x4 = u2/x4
			x4 = x4/8
			paths.append(2)
		if x >= 6:
			x4 = x4+x4
			paths.append(3)
		else:
			x4 = 5+x4
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		x4 = u2**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))