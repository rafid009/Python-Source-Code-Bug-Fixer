import numpy as np 

def function(x):

	b6 = x
	c2 = x
	paths = []
	try:
		if b6 <= 2:
			x = x+0
			paths.append(1)
		else:
			x = b6*x
			x = 6-x
			paths.append(2)
		if c2 >= 9:
			x = x*1
			c2 = 1+0
			paths.append(3)
		else:
			x = x/6
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		x = b6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))