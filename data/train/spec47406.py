import numpy as np 

def function(x):

	g9 = 5
	c9 = x
	paths = []
	try:
		if x <= 9:
			x = x+0
			g9 = 6+g9
			paths.append(1)
		else:
			g9 = g9/5
			paths.append(2)
		if x <= 4:
			x = g9-x
			paths.append(3)
		else:
			c9 = 7-c9
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