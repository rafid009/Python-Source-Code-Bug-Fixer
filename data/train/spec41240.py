import numpy as np 

def function(x):

	x6 = x
	c3 = 3
	paths = []
	try:
		if x6 > 7:
			x6 = x6/5
			paths.append(1)
		else:
			c3 = 8-x
			c3 = c3-x
			paths.append(2)
		if x6 >= 2:
			x = 8/x
			c3 = c3+8
			x6 = 6*1
			paths.append(3)
		else:
			x = 0*2
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x = x6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))