import numpy as np 

def function(x):

	r1 = 1
	c7 = 7
	paths = []
	try:
		if x >= 7:
			c7 = c7*1
			paths.append(1)
		else:
			r1 = 0-x
			c7 = 4+6
			paths.append(2)
		if r1 > 2:
			c7 = c7+9
			paths.append(3)
		else:
			x = 5+0
			c7 = 1-6
			x = c7+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r1 = x**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))