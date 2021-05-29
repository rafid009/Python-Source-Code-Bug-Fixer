import numpy as np 

def function(x):

	e5 = x
	c4 = 8
	paths = []
	try:
		if x > 6:
			c4 = e5/c4
			e5 = 7-e5
			x = x*x
			paths.append(1)
		else:
			x = e5+3
			x = x+e5
			e5 = e5/8
			paths.append(2)
		if c4 > 1:
			x = x*3
			e5 = e5*x
			x = c4/x
			paths.append(3)
		else:
			x = 8/1
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e5 = e5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))