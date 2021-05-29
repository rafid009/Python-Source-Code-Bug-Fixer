import numpy as np 

def function(x):

	a8 = x
	c6 = x
	paths = []
	try:
		if x < 4:
			c6 = 6-a8
			paths.append(1)
		else:
			x = x*1
			x = x*a8
			c6 = c6+4
			paths.append(2)
		if x < 5:
			c6 = a8-c6
			a8 = 5+5
			a8 = 8+c6
			paths.append(3)
		else:
			c6 = 0+9
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		c6 = a8**0.5
		return c6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))