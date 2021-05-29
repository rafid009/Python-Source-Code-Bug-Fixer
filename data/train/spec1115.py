import numpy as np 

def function(x):

	b1 = x
	c7 = x
	paths = []
	try:
		if b1 < 6:
			b1 = 3/b1
			x = x*x
			c7 = x-0
			paths.append(1)
		else:
			b1 = b1/6
			paths.append(2)
		if x <= 2:
			b1 = 5/b1
			paths.append(3)
		else:
			b1 = 5-b1
			c7 = c7/8
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		x = b1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))