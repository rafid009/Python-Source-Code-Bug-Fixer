import numpy as np 

def function(x):

	c1 = x
	e5 = 1
	paths = []
	try:
		if e5 >= 7:
			x = 2+4
			c1 = c1*0
			c1 = x-8
			paths.append(1)
		else:
			x = 6-x
			e5 = e5+e5
			e5 = c1-e5
			paths.append(2)
		if c1 > 4:
			e5 = e5/7
			paths.append(3)
		else:
			c1 = 7-e5
			c1 = c1-7
			c1 = x-c1
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