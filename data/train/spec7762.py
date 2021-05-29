import numpy as np 

def function(x):

	c9 = x
	c8 = x
	paths = []
	try:
		if c8 < 1:
			x = c9/3
			paths.append(1)
		else:
			x = x+c9
			c8 = 5/c8
			paths.append(2)
		if x <= 5:
			c8 = c8/6
			x = x*x
			paths.append(3)
		else:
			x = 6*1
			x = 3/5
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		c9 = c9**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))