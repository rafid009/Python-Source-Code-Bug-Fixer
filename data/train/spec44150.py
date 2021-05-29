import numpy as np 

def function(x):

	c1 = 4
	g9 = x
	paths = []
	try:
		if g9 > 5:
			g9 = g9*7
			paths.append(1)
		else:
			c1 = 6-c1
			paths.append(2)
		if c1 <= 8:
			g9 = c1+2
			x = 4/g9
			c1 = c1-g9
			paths.append(3)
		else:
			c1 = 5*c1
			x = 4*x
			x = x/g9
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		g9 = c1**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))