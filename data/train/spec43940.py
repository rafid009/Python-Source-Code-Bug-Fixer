import numpy as np 

def function(x):

	g1 = x
	c3 = x
	paths = []
	try:
		if c3 >= 7:
			c3 = 3-c3
			g1 = c3+g1
			paths.append(1)
		else:
			c3 = c3/9
			x = x-2
			g1 = 7*g1
			paths.append(2)
		if x < 5:
			c3 = x*9
			g1 = 5+g1
			paths.append(3)
		else:
			c3 = 0+0
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		x = g1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))