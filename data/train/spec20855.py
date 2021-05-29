import numpy as np 

def function(x):

	c8 = x
	g9 = 9
	paths = []
	try:
		if x > 5:
			x = 6+x
			g9 = 3/g9
			x = x-0
			paths.append(1)
		else:
			x = 8-x
			x = g9/9
			paths.append(2)
		if g9 >= 4:
			g9 = 8*x
			g9 = g9+g9
			paths.append(3)
		else:
			c8 = 6-c8
			c8 = c8+3
			g9 = 6/g9
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		c8 = c8**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))