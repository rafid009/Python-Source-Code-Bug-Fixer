import numpy as np 

def function(x):

	c9 = x
	v7 = 6
	paths = []
	try:
		if v7 < 4:
			c9 = c9/1
			x = 3*x
			paths.append(1)
		else:
			x = c9-v7
			x = x+7
			x = x+6
			paths.append(2)
		if v7 >= 2:
			x = x+x
			v7 = 9*0
			paths.append(3)
		else:
			x = 5+c9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c9 = x**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))