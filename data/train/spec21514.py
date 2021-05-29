import numpy as np 

def function(x):

	x1 = 8
	v4 = x
	paths = []
	try:
		if x1 < 6:
			x1 = x1-8
			x = v4/v4
			paths.append(1)
		else:
			x1 = x1*3
			paths.append(2)
		if v4 > 3:
			x = x1-3
			x = v4*1
			paths.append(3)
		else:
			v4 = v4/v4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v4 = x**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))