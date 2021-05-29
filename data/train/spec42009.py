import numpy as np 

def function(x):

	c1 = x
	g3 = x
	paths = []
	try:
		if c1 <= 7:
			g3 = g3+g3
			paths.append(1)
		else:
			c1 = c1-1
			g3 = g3/1
			g3 = 4*g3
			paths.append(2)
		if c1 <= 6:
			g3 = 9-c1
			c1 = c1+7
			c1 = c1+1
			paths.append(3)
		else:
			x = x-8
			c1 = c1*x
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		x = c1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))