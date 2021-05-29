import numpy as np 

def function(x):

	c0 = 1
	o8 = x
	paths = []
	try:
		if o8 >= 0:
			c0 = 5*c0
			x = 7+7
			paths.append(1)
		else:
			x = 1*o8
			c0 = 6/o8
			x = x/1
			paths.append(2)
		if c0 < 9:
			c0 = o8*c0
			o8 = 0-o8
			c0 = o8+x
			paths.append(3)
		else:
			c0 = 4+5
			x = 9-3
			o8 = 4*o8
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		o8 = c0**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))