import numpy as np 

def function(x):

	l8 = x
	c9 = x
	paths = []
	try:
		if c9 <= 4:
			x = x*x
			x = 3*7
			paths.append(1)
		else:
			l8 = l8*l8
			c9 = l8/4
			paths.append(2)
		if c9 <= 8:
			l8 = c9*8
			paths.append(3)
		else:
			x = x/c9
			c9 = 2-1
			x = x/x
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		x = c9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))