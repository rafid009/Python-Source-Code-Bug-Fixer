import numpy as np 

def function(x):

	v1 = 1
	x4 = x
	paths = []
	try:
		if v1 > 2:
			x4 = x4-x4
			v1 = v1*v1
			paths.append(1)
		else:
			x = v1*7
			paths.append(2)
		if x >= 9:
			x4 = 0*x4
			x = x*9
			x4 = 9*v1
			paths.append(3)
		else:
			x4 = 1*x4
			x4 = v1-x
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x4 = x4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))