import numpy as np 

def function(x):

	a3 = x
	c6 = x
	paths = []
	try:
		if c6 < 2:
			a3 = 9-2
			c6 = c6+7
			paths.append(1)
		else:
			x = x*8
			paths.append(2)
		if c6 >= 5:
			c6 = 0/6
			c6 = a3*6
			x = 0-x
			paths.append(3)
		else:
			x = 3/a3
			x = c6*6
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		x = c6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))