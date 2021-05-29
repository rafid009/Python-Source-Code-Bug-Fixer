import numpy as np 

def function(x):

	o8 = 6
	c4 = x
	paths = []
	try:
		if c4 >= 9:
			c4 = 5-o8
			paths.append(1)
		else:
			o8 = 3/7
			o8 = o8/x
			c4 = 0/c4
			paths.append(2)
		if o8 > 1:
			c4 = 5/6
			o8 = o8/9
			x = o8*x
			paths.append(3)
		else:
			c4 = c4-2
			o8 = 1/8
			o8 = 2/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o8 = x**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))