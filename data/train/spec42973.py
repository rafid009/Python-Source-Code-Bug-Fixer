import numpy as np 

def function(x):

	j1 = x
	c7 = 3
	paths = []
	try:
		if j1 <= 5:
			c7 = j1*7
			c7 = c7/9
			c7 = 3*c7
			paths.append(1)
		else:
			j1 = 7*j1
			x = c7*1
			c7 = c7*c7
			paths.append(2)
		if j1 <= 4:
			x = 4/x
			paths.append(3)
		else:
			j1 = j1*6
			x = j1-2
			c7 = 6*c7
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