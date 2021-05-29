import numpy as np 

def function(x):

	c2 = 5
	x4 = 8
	paths = []
	try:
		if x4 >= 4:
			x4 = 8*x4
			x4 = 3+x4
			paths.append(1)
		else:
			x4 = 7/5
			x = 8+1
			paths.append(2)
		if c2 > 4:
			x4 = 9-x4
			paths.append(3)
		else:
			c2 = 6/4
			c2 = c2*0
			x = x/c2
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x = x4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))