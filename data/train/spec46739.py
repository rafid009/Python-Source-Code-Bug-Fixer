import numpy as np 

def function(x):

	a8 = 0
	c1 = x
	paths = []
	try:
		if x <= 6:
			a8 = a8+2
			paths.append(1)
		else:
			a8 = 7*a8
			a8 = 3-9
			c1 = c1-9
			paths.append(2)
		if x <= 5:
			x = 6-x
			paths.append(3)
		else:
			c1 = 9*c1
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))