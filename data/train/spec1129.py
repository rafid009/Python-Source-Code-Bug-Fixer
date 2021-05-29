import numpy as np 

def function(x):

	i8 = x
	c2 = 9
	paths = []
	try:
		if x <= 4:
			x = 4/2
			paths.append(1)
		else:
			x = 7-x
			c2 = 6-6
			x = x*1
			paths.append(2)
		if i8 < 0:
			x = x-x
			c2 = c2+9
			i8 = 3/i8
			paths.append(3)
		else:
			c2 = c2*6
			c2 = 4-i8
			i8 = i8+c2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c2 = x**0.5
		return c2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))