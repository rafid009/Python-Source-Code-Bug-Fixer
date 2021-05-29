import numpy as np 

def function(x):

	c6 = x
	i3 = 9
	paths = []
	try:
		if x < 7:
			c6 = c6/3
			paths.append(1)
		else:
			c6 = i3+x
			i3 = 1-4
			c6 = c6*x
			paths.append(2)
		if c6 <= 1:
			i3 = i3*3
			x = x*c6
			paths.append(3)
		else:
			c6 = 3*c6
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		c6 = i3**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))