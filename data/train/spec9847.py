import numpy as np 

def function(x):

	c7 = x
	c9 = x
	paths = []
	try:
		if c9 > 2:
			c7 = 8+1
			x = c7*0
			paths.append(1)
		else:
			c7 = c7/4
			paths.append(2)
		if c7 >= 5:
			c9 = 9-9
			c9 = x-2
			paths.append(3)
		else:
			x = 7+9
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