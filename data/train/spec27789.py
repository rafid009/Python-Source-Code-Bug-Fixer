import numpy as np 

def function(x):

	k4 = 3
	u4 = x
	paths = []
	try:
		if x <= 0:
			u4 = u4/x
			k4 = k4*x
			x = u4-4
			paths.append(1)
		else:
			u4 = 6+u4
			paths.append(2)
		if k4 > 7:
			x = 6/x
			k4 = 1/x
			k4 = k4*1
			paths.append(3)
		else:
			u4 = 1-8
			u4 = 2/k4
			k4 = k4-u4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))