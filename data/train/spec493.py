import numpy as np 

def function(x):

	c9 = x
	v1 = x
	paths = []
	try:
		if x < 5:
			c9 = v1*1
			x = x*v1
			v1 = v1-2
			paths.append(1)
		else:
			x = 2+x
			paths.append(2)
		if c9 <= 5:
			v1 = x/v1
			paths.append(3)
		else:
			c9 = c9-x
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