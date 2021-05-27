import numpy as np 

def function(x):

	v1 = 9
	c3 = x
	paths = []
	try:
		if c3 < 5:
			v1 = v1/7
			c3 = c3+6
			paths.append(1)
		else:
			c3 = x+8
			x = v1*1
			paths.append(2)
		if v1 > 9:
			x = 2/x
			v1 = 8-v1
			c3 = c3-3
			paths.append(3)
		else:
			c3 = v1-c3
			v1 = 9+v1
			v1 = 3-v1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v1 = x**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))