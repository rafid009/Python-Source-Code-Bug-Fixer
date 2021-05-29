import numpy as np 

def function(x):

	c1 = x
	x6 = x
	paths = []
	try:
		if c1 > 7:
			x6 = c1*5
			x = 2+3
			paths.append(1)
		else:
			x = 9-x
			x6 = x6+9
			paths.append(2)
		if x <= 7:
			c1 = 8-c1
			paths.append(3)
		else:
			x6 = x6+2
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