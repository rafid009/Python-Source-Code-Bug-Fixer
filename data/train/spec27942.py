import numpy as np 

def function(x):

	c7 = x
	e6 = 5
	paths = []
	try:
		if x < 4:
			x = 0*4
			paths.append(1)
		else:
			x = e6/x
			c7 = 9/c7
			e6 = e6*4
			paths.append(2)
		if e6 > 7:
			x = x-1
			paths.append(3)
		else:
			e6 = 3-e6
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		e6 = e6**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))