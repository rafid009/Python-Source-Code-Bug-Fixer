import numpy as np 

def function(x):

	c3 = 6
	v8 = x
	paths = []
	try:
		if x <= 6:
			c3 = 8+x
			x = 6-1
			paths.append(1)
		else:
			c3 = c3+3
			c3 = v8/c3
			paths.append(2)
		if x <= 6:
			v8 = 4*v8
			x = c3+v8
			c3 = c3*0
			paths.append(3)
		else:
			x = x/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c3 = x**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))