import numpy as np 

def function(x):

	b4 = x
	c6 = 0
	paths = []
	try:
		if c6 >= 6:
			c6 = c6-c6
			paths.append(1)
		else:
			b4 = c6*c6
			c6 = b4-3
			paths.append(2)
		if b4 <= 0:
			b4 = c6+b4
			paths.append(3)
		else:
			c6 = b4+9
			c6 = c6-9
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))