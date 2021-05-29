import numpy as np 

def function(x):

	u3 = 0
	c4 = x
	paths = []
	try:
		if x <= 2:
			u3 = u3-u3
			paths.append(1)
		else:
			x = 1/x
			paths.append(2)
		if u3 >= 7:
			c4 = 3*x
			x = 2/x
			paths.append(3)
		else:
			x = 5/x
			c4 = c4*1
			x = x-1
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		c4 = c4**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))