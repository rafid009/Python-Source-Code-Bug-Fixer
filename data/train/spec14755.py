import numpy as np 

def function(x):

	v4 = 5
	x3 = 6
	paths = []
	try:
		if x < 5:
			x = 2-x
			v4 = 6-v4
			paths.append(1)
		else:
			x3 = 0-x3
			x3 = 8-0
			x3 = x3*2
			paths.append(2)
		if x > 5:
			x3 = x3/5
			paths.append(3)
		else:
			x = x-7
			v4 = 3-9
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