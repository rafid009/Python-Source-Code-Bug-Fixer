import numpy as np 

def function(x):

	u6 = 9
	c4 = x
	paths = []
	try:
		if c4 > 9:
			x = x/3
			u6 = 6-u6
			paths.append(1)
		else:
			c4 = 2-c4
			u6 = u6*3
			c4 = 3/c4
			paths.append(2)
		if x > 0:
			c4 = 7+3
			x = 9/c4
			c4 = u6*2
			paths.append(3)
		else:
			x = 7*x
			x = 4-x
			x = x-x
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		x = c4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))