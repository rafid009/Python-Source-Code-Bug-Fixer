import numpy as np 

def function(x):

	c8 = x
	e3 = 7
	paths = []
	try:
		if x >= 3:
			c8 = 3-c8
			paths.append(1)
		else:
			e3 = e3+5
			e3 = e3/9
			e3 = 9-7
			paths.append(2)
		if c8 >= 5:
			c8 = 7/c8
			e3 = e3-9
			e3 = x+e3
			paths.append(3)
		else:
			x = 9/3
			c8 = c8-1
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))