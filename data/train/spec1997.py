import numpy as np 

def function(x):

	o4 = 9
	c8 = 1
	paths = []
	try:
		if o4 <= 6:
			o4 = 4+8
			x = 4-o4
			o4 = o4-9
			paths.append(1)
		else:
			o4 = o4-3
			o4 = o4/c8
			paths.append(2)
		if x <= 6:
			c8 = x/x
			o4 = o4*2
			paths.append(3)
		else:
			o4 = 6-8
			o4 = o4+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o4 = x**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))