import numpy as np 

def function(x):

	c4 = 1
	e7 = x
	paths = []
	try:
		if x >= 8:
			e7 = x/7
			e7 = 4/e7
			paths.append(1)
		else:
			c4 = e7+c4
			x = x-2
			x = x-6
			paths.append(2)
		if e7 > 0:
			c4 = 3+2
			paths.append(3)
		else:
			x = x*e7
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