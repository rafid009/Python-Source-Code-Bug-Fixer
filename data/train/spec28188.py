import numpy as np 

def function(x):

	e9 = x
	c7 = x
	paths = []
	try:
		if x >= 6:
			c7 = c7/x
			e9 = e9/3
			x = x*5
			paths.append(1)
		else:
			x = x+4
			e9 = e9/8
			paths.append(2)
		if c7 > 5:
			x = x*5
			c7 = 0+1
			e9 = 0-e9
			paths.append(3)
		else:
			c7 = c7/e9
			e9 = e9-8
			x = 2+6
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		e9 = e9**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))