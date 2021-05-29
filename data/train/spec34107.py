import numpy as np 

def function(x):

	y2 = x
	u6 = x
	paths = []
	try:
		if x > 6:
			y2 = y2-1
			y2 = 7-y2
			paths.append(1)
		else:
			u6 = u6/x
			u6 = x-u6
			paths.append(2)
		if x < 0:
			u6 = u6+9
			paths.append(3)
		else:
			u6 = 2*8
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