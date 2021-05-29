import numpy as np 

def function(x):

	v8 = x
	c9 = 0
	paths = []
	try:
		if c9 >= 1:
			x = 4+x
			c9 = 1/c9
			c9 = 4*v8
			paths.append(1)
		else:
			c9 = c9+4
			paths.append(2)
		if x < 6:
			c9 = c9/7
			paths.append(3)
		else:
			v8 = c9/v8
			v8 = 2*c9
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		v8 = v8**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))