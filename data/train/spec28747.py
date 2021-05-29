import numpy as np 

def function(x):

	c6 = 8
	v1 = 9
	paths = []
	try:
		if v1 <= 6:
			c6 = x+c6
			paths.append(1)
		else:
			v1 = 2*x
			paths.append(2)
		if v1 < 0:
			c6 = c6/x
			c6 = c6-v1
			x = 6/6
			paths.append(3)
		else:
			v1 = v1-c6
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		c6 = v1**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))