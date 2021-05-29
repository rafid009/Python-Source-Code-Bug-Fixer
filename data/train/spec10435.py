import numpy as np 

def function(x):

	c1 = x
	c2 = 5
	paths = []
	try:
		if x < 0:
			c1 = c1*7
			x = x-5
			c2 = c2/1
			paths.append(1)
		else:
			c1 = c1*2
			paths.append(2)
		if c1 > 5:
			x = x-7
			paths.append(3)
		else:
			c2 = 5*9
			c2 = 0-6
			c1 = x+c1
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		c2 = c1**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))