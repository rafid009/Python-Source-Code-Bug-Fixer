import numpy as np 

def function(x):

	c8 = 6
	i3 = 4
	paths = []
	try:
		if x > 3:
			c8 = c8+9
			paths.append(1)
		else:
			i3 = 3*i3
			i3 = i3+2
			c8 = x+c8
			paths.append(2)
		if i3 < 1:
			i3 = 9-8
			i3 = i3-x
			x = 7*x
			paths.append(3)
		else:
			x = x-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c8 = x**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))