import numpy as np 

def function(x):

	v4 = x
	c9 = 5
	paths = []
	try:
		if c9 >= 6:
			x = x-2
			c9 = v4+5
			paths.append(1)
		else:
			v4 = v4*9
			x = 2*1
			v4 = 7-9
			paths.append(2)
		if v4 > 5:
			v4 = c9-v4
			c9 = 3*c9
			paths.append(3)
		else:
			v4 = 3*v4
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		x = v4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))