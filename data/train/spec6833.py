import numpy as np 

def function(x):

	c6 = x
	r9 = 6
	paths = []
	try:
		if r9 <= 8:
			r9 = r9/r9
			x = c6*x
			r9 = r9+6
			paths.append(1)
		else:
			c6 = 5+4
			c6 = c6-9
			paths.append(2)
		if r9 >= 4:
			r9 = 1-r9
			c6 = c6-5
			paths.append(3)
		else:
			c6 = 5/x
			c6 = 4*c6
			x = x-6
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		x = r9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))