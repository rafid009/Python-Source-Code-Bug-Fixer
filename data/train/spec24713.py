import numpy as np 

def function(x):

	u3 = x
	c8 = 7
	paths = []
	try:
		if u3 > 1:
			u3 = c8+4
			paths.append(1)
		else:
			u3 = 3-u3
			c8 = c8*4
			paths.append(2)
		if c8 >= 4:
			u3 = 3+1
			c8 = c8-x
			paths.append(3)
		else:
			u3 = u3/c8
			c8 = c8+c8
			c8 = c8/u3
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