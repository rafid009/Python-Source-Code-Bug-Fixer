import numpy as np 

def function(x):

	c4 = x
	r9 = 2
	paths = []
	try:
		if x < 8:
			r9 = 5-1
			c4 = c4-1
			x = r9-x
			paths.append(1)
		else:
			c4 = c4*9
			paths.append(2)
		if c4 <= 5:
			r9 = r9*0
			r9 = 2-r9
			paths.append(3)
		else:
			c4 = r9+0
			r9 = r9/3
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