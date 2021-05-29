import numpy as np 

def function(x):

	v4 = x
	x3 = 9
	x = 8
	paths = []
	try:
		if x > 0:
			x = 6-x
			v4 = 7/6
			paths.append(1)
		else:
			x3 = x3*x
			v4 = 4-v4
			paths.append(2)
		if x3 >= 0:
			v4 = x/v4
			x = x/x3
			x = x-v4
			paths.append(3)
		else:
			x3 = v4-v4
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		x = v4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))