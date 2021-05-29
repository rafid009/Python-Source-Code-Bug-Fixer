import numpy as np 

def function(x):

	c2 = 5
	v6 = x
	paths = []
	try:
		if x > 2:
			v6 = 9-x
			v6 = v6+7
			paths.append(1)
		else:
			c2 = 7-2
			c2 = c2+v6
			paths.append(2)
		if c2 < 2:
			v6 = v6+3
			paths.append(3)
		else:
			c2 = c2/4
			v6 = v6/5
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		c2 = c2**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))