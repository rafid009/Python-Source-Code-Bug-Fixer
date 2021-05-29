import numpy as np 

def function(x):

	e4 = x
	c5 = x
	paths = []
	try:
		if x <= 7:
			c5 = c5/9
			c5 = 9*e4
			paths.append(1)
		else:
			c5 = 6*c5
			x = 3+e4
			paths.append(2)
		if c5 < 6:
			e4 = e4*0
			paths.append(3)
		else:
			e4 = e4-1
			x = e4/5
			e4 = 3-e4
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		c5 = c5**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))