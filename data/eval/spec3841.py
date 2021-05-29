import numpy as np 

def function(x):

	a8 = 9
	c4 = x
	paths = []
	try:
		if c4 <= 7:
			x = x/7
			paths.append(1)
		else:
			c4 = 9*c4
			c4 = 2-9
			paths.append(2)
		if x >= 0:
			a8 = 3-a8
			paths.append(3)
		else:
			a8 = a8-0
			c4 = x/x
			a8 = 0*1
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		a8 = a8**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))