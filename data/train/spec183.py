import numpy as np 

def function(x):

	c5 = 8
	u5 = x
	paths = []
	try:
		if x > 1:
			c5 = x/c5
			x = x/c5
			paths.append(1)
		else:
			c5 = 7-c5
			paths.append(2)
		if x > 7:
			c5 = c5*2
			u5 = u5/u5
			paths.append(3)
		else:
			u5 = 1*u5
			u5 = 7/u5
			x = 2/6
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		c5 = c5**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))