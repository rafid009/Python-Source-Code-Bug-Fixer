import numpy as np 

def function(x):

	v3 = 7
	c7 = x
	paths = []
	try:
		if x <= 5:
			c7 = x+7
			paths.append(1)
		else:
			x = x-6
			v3 = 3+v3
			x = x-1
			paths.append(2)
		if v3 >= 2:
			v3 = v3+c7
			v3 = c7/4
			v3 = c7/1
			paths.append(3)
		else:
			x = x+1
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