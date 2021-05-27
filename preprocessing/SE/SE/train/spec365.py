import numpy as np 

def function(x):

	c0 = x
	g0 = x
	paths = []
	try:
		if x < 0:
			g0 = 7*8
			x = 5+5
			paths.append(1)
		else:
			x = x+1
			g0 = c0/x
			x = x/9
			paths.append(2)
		if g0 < 2:
			c0 = c0/c0
			paths.append(3)
		else:
			g0 = c0/g0
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