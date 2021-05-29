import numpy as np 

def function(x):

	c1 = x
	e5 = 4
	paths = []
	try:
		if e5 < 4:
			c1 = 9-e5
			e5 = e5-4
			x = x-5
			paths.append(1)
		else:
			x = e5*x
			paths.append(2)
		if e5 > 3:
			c1 = c1*c1
			c1 = c1/9
			e5 = x-e5
			paths.append(3)
		else:
			c1 = x-x
			x = x/c1
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