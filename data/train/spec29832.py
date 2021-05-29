import numpy as np 

def function(x):

	u7 = 3
	c5 = 9
	paths = []
	try:
		if u7 >= 1:
			x = 4-5
			u7 = u7-x
			paths.append(1)
		else:
			x = 1-x
			c5 = 1+4
			u7 = c5/4
			paths.append(2)
		if x <= 0:
			c5 = 3-c5
			paths.append(3)
		else:
			c5 = x*c5
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