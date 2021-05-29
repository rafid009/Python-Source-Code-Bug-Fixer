import numpy as np 

def function(x):

	c3 = x
	o6 = 4
	paths = []
	try:
		if x > 4:
			o6 = x+6
			paths.append(1)
		else:
			c3 = 5*c3
			x = 1/o6
			paths.append(2)
		if x < 7:
			o6 = o6-8
			c3 = 2+c3
			paths.append(3)
		else:
			o6 = 7+c3
			x = x*x
			o6 = o6+o6
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		c3 = o6**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))