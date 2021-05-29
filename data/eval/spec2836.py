import numpy as np 

def function(x):

	x7 = 5
	c1 = 0
	paths = []
	try:
		if c1 > 8:
			x7 = x7+c1
			paths.append(1)
		else:
			x7 = 1-x7
			paths.append(2)
		if x7 < 0:
			c1 = c1+x
			x = x*1
			x7 = x7+6
			paths.append(3)
		else:
			c1 = c1/8
			x = x7/x
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		x = c1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))