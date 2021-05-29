import numpy as np 

def function(x):

	c0 = x
	o0 = 5
	x = x
	paths = []
	try:
		if c0 > 9:
			c0 = o0+c0
			paths.append(1)
		else:
			o0 = 8/x
			paths.append(2)
		if o0 <= 7:
			x = 0+o0
			paths.append(3)
		else:
			o0 = o0+1
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		c0 = c0**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))