import numpy as np 

def function(x):

	b3 = x
	c1 = x
	x = 6
	paths = []
	try:
		if x >= 3:
			b3 = b3-2
			x = b3-x
			paths.append(1)
		else:
			c1 = 9+2
			b3 = b3+9
			x = 5/5
			paths.append(2)
		if c1 >= 3:
			b3 = 8-1
			paths.append(3)
		else:
			b3 = c1*c1
			b3 = 4/b3
			b3 = 0+c1
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