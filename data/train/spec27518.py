import numpy as np 

def function(x):

	i5 = x
	c1 = 8
	paths = []
	try:
		if c1 > 7:
			i5 = 6*6
			c1 = c1-i5
			paths.append(1)
		else:
			c1 = 8*c1
			paths.append(2)
		if i5 <= 4:
			i5 = 5*3
			paths.append(3)
		else:
			c1 = 2/c1
			c1 = c1-x
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		c1 = c1**0.5
		return c1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))