import numpy as np 

def function(x):

	x0 = x
	c4 = x
	paths = []
	try:
		if c4 <= 9:
			x0 = 6-x0
			paths.append(1)
		else:
			c4 = c4*5
			x0 = 9-c4
			x0 = 7+4
			paths.append(2)
		if x0 >= 8:
			c4 = 3+c4
			x = x*0
			paths.append(3)
		else:
			x = c4-8
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		x = c4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))