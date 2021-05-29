import numpy as np 

def function(x):

	v7 = 8
	c8 = 3
	paths = []
	try:
		if x <= 5:
			v7 = v7/c8
			paths.append(1)
		else:
			v7 = 3*c8
			v7 = 1-3
			paths.append(2)
		if c8 > 6:
			v7 = c8-v7
			v7 = 6/1
			paths.append(3)
		else:
			x = x/4
			x = c8/x
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		x = v7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))