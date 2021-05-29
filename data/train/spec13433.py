import numpy as np 

def function(x):

	c9 = x
	b3 = x
	paths = []
	try:
		if b3 > 5:
			x = b3*6
			b3 = 2*4
			c9 = c9+7
			paths.append(1)
		else:
			c9 = 3/3
			paths.append(2)
		if x < 5:
			x = c9+x
			paths.append(3)
		else:
			c9 = 5*c9
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