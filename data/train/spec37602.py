import numpy as np 

def function(x):

	o2 = 3
	c9 = x
	paths = []
	try:
		if x < 9:
			o2 = 1/6
			c9 = 4-c9
			paths.append(1)
		else:
			o2 = x-o2
			c9 = o2+7
			c9 = 6+c9
			paths.append(2)
		if c9 > 1:
			o2 = x*o2
			paths.append(3)
		else:
			x = c9-x
			c9 = 9/5
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		c9 = o2**0.5
		return c9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))