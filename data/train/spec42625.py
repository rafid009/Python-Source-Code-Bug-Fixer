import numpy as np 

def function(x):

	c8 = 5
	o0 = 2
	paths = []
	try:
		if x < 9:
			c8 = o0-c8
			c8 = c8*4
			o0 = c8+c8
			paths.append(1)
		else:
			c8 = 5-c8
			c8 = c8*2
			o0 = o0+c8
			paths.append(2)
		if x <= 1:
			o0 = o0+c8
			o0 = 4-6
			paths.append(3)
		else:
			o0 = 9/o0
			o0 = 6*9
			o0 = 3+o0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))