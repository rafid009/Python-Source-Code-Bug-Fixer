import numpy as np 

def function(x):

	c7 = x
	x9 = 1
	paths = []
	try:
		if c7 < 8:
			c7 = 7+c7
			paths.append(1)
		else:
			x9 = x9/c7
			c7 = 3-c7
			x9 = 1*0
			paths.append(2)
		if x9 <= 6:
			x = x+x
			paths.append(3)
		else:
			x = x9*5
			c7 = c7-1
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