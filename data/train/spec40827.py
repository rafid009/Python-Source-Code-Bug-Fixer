import numpy as np 

def function(x):

	c7 = 2
	o2 = 5
	x = x
	paths = []
	try:
		if o2 >= 5:
			c7 = c7*1
			paths.append(1)
		else:
			o2 = 5*o2
			x = o2/3
			o2 = o2+9
			paths.append(2)
		if x < 5:
			o2 = 1-o2
			paths.append(3)
		else:
			c7 = x*o2
			x = x+c7
			c7 = 9*c7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		c7 = x**0.5
		return c7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))