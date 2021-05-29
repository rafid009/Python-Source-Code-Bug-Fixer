import numpy as np 

def function(x):

	x1 = x
	c3 = x
	paths = []
	try:
		if x1 < 1:
			x = c3+x
			x = x+3
			paths.append(1)
		else:
			x1 = 3+x1
			x1 = 2+c3
			c3 = 4-2
			paths.append(2)
		if x1 <= 4:
			c3 = c3-x
			paths.append(3)
		else:
			x1 = x1-x
			x = x*c3
			x = 9-8
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x = x1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))