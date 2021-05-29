import numpy as np 

def function(x):

	c6 = 8
	v3 = x
	paths = []
	try:
		if c6 >= 2:
			c6 = c6+7
			c6 = 9*v3
			paths.append(1)
		else:
			c6 = 6*0
			paths.append(2)
		if v3 <= 7:
			c6 = c6/4
			paths.append(3)
		else:
			x = c6/4
			v3 = 8-v3
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		c6 = c6**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))