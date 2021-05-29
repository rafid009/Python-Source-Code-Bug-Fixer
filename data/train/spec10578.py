import numpy as np 

def function(x):

	c4 = 9
	a0 = x
	paths = []
	try:
		if c4 >= 6:
			x = x/4
			c4 = 0+c4
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if x < 6:
			c4 = 5+c4
			a0 = 7*a0
			paths.append(3)
		else:
			c4 = c4-7
			c4 = c4*x
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		a0 = a0**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))