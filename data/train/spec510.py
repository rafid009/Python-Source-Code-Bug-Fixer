import numpy as np 

def function(x):

	g2 = 3
	c0 = x
	paths = []
	try:
		if c0 <= 0:
			x = x*6
			paths.append(1)
		else:
			c0 = 7-0
			x = x/8
			paths.append(2)
		if c0 > 7:
			g2 = 1+g2
			g2 = 3+g2
			g2 = 6-3
			paths.append(3)
		else:
			g2 = 7*1
			g2 = 1*c0
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		c0 = c0**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))