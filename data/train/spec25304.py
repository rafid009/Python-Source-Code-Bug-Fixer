import numpy as np 

def function(x):

	j1 = x
	c4 = x
	paths = []
	try:
		if j1 <= 8:
			x = 8-j1
			paths.append(1)
		else:
			j1 = j1-4
			c4 = j1/c4
			j1 = j1*8
			paths.append(2)
		if j1 < 0:
			j1 = x/j1
			paths.append(3)
		else:
			x = x/c4
			j1 = j1-7
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