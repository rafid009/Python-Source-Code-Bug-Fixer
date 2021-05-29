import numpy as np 

def function(x):

	c4 = x
	r9 = x
	paths = []
	try:
		if r9 < 2:
			r9 = r9/4
			x = c4-x
			c4 = 6+r9
			paths.append(1)
		else:
			r9 = 7/6
			c4 = 9-c4
			x = 6-2
			paths.append(2)
		if x >= 6:
			c4 = x-r9
			x = x-1
			paths.append(3)
		else:
			c4 = 6*0
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		c4 = r9**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))