import numpy as np 

def function(x):

	v1 = x
	x4 = 1
	paths = []
	try:
		if v1 <= 2:
			x = 5+x
			paths.append(1)
		else:
			x4 = 0*x4
			v1 = v1/x
			paths.append(2)
		if x4 < 0:
			x4 = x4+3
			x4 = 0-5
			x = x+5
			paths.append(3)
		else:
			v1 = 7/v1
			x = 5+x4
			x4 = 3*v1
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x = x4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))