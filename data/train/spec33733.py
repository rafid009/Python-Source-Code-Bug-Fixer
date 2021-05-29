import numpy as np 

def function(x):

	v8 = 5
	c4 = x
	paths = []
	try:
		if c4 >= 4:
			v8 = 2*v8
			x = 0*x
			paths.append(1)
		else:
			v8 = v8*2
			v8 = 3-v8
			x = c4/8
			paths.append(2)
		if x < 9:
			c4 = x/6
			paths.append(3)
		else:
			v8 = 2-v8
			c4 = c4+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c4 = x**0.5
		return c4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))