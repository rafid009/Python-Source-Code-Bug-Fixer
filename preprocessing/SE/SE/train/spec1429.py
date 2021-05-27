import numpy as np 

def function(x):

	y5 = x
	k4 = 3
	paths = []
	try:
		if x >= 8:
			y5 = 0-y5
			paths.append(1)
		else:
			x = 8/x
			k4 = 0*k4
			k4 = k4-0
			paths.append(2)
		if x <= 9:
			k4 = y5-k4
			paths.append(3)
		else:
			x = x*9
			k4 = k4*k4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))