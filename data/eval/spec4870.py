import numpy as np 

def function(x):

	j3 = 9
	c7 = x
	paths = []
	try:
		if c7 >= 6:
			c7 = c7-9
			paths.append(1)
		else:
			c7 = c7+j3
			x = 6*x
			j3 = 4-9
			paths.append(2)
		if j3 <= 1:
			j3 = j3-6
			c7 = c7*9
			paths.append(3)
		else:
			j3 = j3/4
			x = 2/j3
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