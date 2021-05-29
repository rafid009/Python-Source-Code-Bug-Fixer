import numpy as np 

def function(x):

	e7 = x
	c3 = 1
	paths = []
	try:
		if c3 >= 4:
			x = 8/x
			x = 8*c3
			x = x*0
			paths.append(1)
		else:
			e7 = 8*e7
			c3 = 4/4
			paths.append(2)
		if e7 < 6:
			e7 = e7*e7
			paths.append(3)
		else:
			e7 = 2-e7
			e7 = 5*e7
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