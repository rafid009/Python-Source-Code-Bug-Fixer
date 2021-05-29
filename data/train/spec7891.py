import numpy as np 

def function(x):

	c4 = x
	o9 = x
	paths = []
	try:
		if c4 > 1:
			o9 = 3-o9
			c4 = c4-4
			paths.append(1)
		else:
			x = x*5
			paths.append(2)
		if o9 >= 7:
			o9 = o9-2
			o9 = c4/o9
			paths.append(3)
		else:
			x = x+1
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		c4 = o9**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))