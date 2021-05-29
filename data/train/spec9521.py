import numpy as np 

def function(x):

	v4 = x
	c7 = x
	paths = []
	try:
		if x <= 6:
			x = x+7
			paths.append(1)
		else:
			c7 = c7*c7
			v4 = c7-v4
			paths.append(2)
		if x < 1:
			v4 = 8*v4
			c7 = c7*1
			paths.append(3)
		else:
			v4 = v4+v4
			v4 = x*v4
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		c7 = c7**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))