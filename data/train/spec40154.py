import numpy as np 

def function(x):

	e7 = x
	c7 = x
	x = 4
	paths = []
	try:
		if x < 8:
			e7 = c7+0
			c7 = c7-x
			paths.append(1)
		else:
			x = x*9
			c7 = 3/3
			x = 9/5
			paths.append(2)
		if c7 <= 1:
			e7 = e7/4
			paths.append(3)
		else:
			x = x+4
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		e7 = e7**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))