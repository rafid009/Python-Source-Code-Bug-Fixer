import numpy as np 

def function(x):

	v1 = x
	c7 = 7
	paths = []
	try:
		if v1 >= 5:
			x = x*v1
			v1 = v1*x
			c7 = 9-c7
			paths.append(1)
		else:
			v1 = v1*0
			paths.append(2)
		if c7 < 7:
			x = 1*2
			paths.append(3)
		else:
			c7 = c7-5
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