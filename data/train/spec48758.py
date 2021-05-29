import numpy as np 

def function(x):

	e0 = x
	u4 = 9
	paths = []
	try:
		if x < 5:
			e0 = 0-u4
			e0 = e0-u4
			paths.append(1)
		else:
			e0 = 1-9
			x = x/4
			x = x+4
			paths.append(2)
		if x <= 1:
			e0 = e0*e0
			x = 4/x
			u4 = u4-u4
			paths.append(3)
		else:
			u4 = u4-x
			e0 = e0-0
			x = x-8
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		x = u4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))