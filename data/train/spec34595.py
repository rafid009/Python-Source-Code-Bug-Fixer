import numpy as np 

def function(x):

	c7 = x
	b3 = x
	paths = []
	try:
		if b3 >= 6:
			x = x-7
			c7 = x*c7
			x = 3+7
			paths.append(1)
		else:
			b3 = b3/6
			paths.append(2)
		if b3 < 6:
			x = c7/x
			b3 = b3*b3
			b3 = 4+1
			paths.append(3)
		else:
			b3 = 3-9
			c7 = 6-x
			c7 = c7-c7
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		x = b3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))