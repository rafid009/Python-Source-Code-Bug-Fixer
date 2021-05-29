import numpy as np 

def function(x):

	c5 = 3
	r9 = 0
	paths = []
	try:
		if c5 < 2:
			c5 = 1*5
			x = 3/r9
			paths.append(1)
		else:
			x = 3+x
			c5 = 1*6
			r9 = r9-9
			paths.append(2)
		if c5 <= 5:
			c5 = r9+c5
			paths.append(3)
		else:
			c5 = c5-c5
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