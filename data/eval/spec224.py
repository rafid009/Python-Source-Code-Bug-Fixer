import numpy as np 

def function(x):

	c7 = 4
	e9 = x
	x = x
	paths = []
	try:
		if x < 2:
			c7 = 9+c7
			paths.append(1)
		else:
			x = e9*3
			e9 = x-1
			e9 = e9-x
			paths.append(2)
		if c7 <= 2:
			x = c7-x
			x = x/x
			paths.append(3)
		else:
			e9 = c7+x
			x = 8-x
			c7 = x-7
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		e9 = c7**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))