import numpy as np 

def function(x):

	i9 = 2
	c7 = x
	paths = []
	try:
		if x <= 5:
			i9 = 0/1
			paths.append(1)
		else:
			i9 = i9/4
			c7 = c7-c7
			c7 = 1+9
			paths.append(2)
		if c7 <= 5:
			c7 = x*2
			x = i9*5
			paths.append(3)
		else:
			x = 2*3
			x = i9+2
			i9 = i9+i9
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