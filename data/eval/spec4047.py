import numpy as np 

def function(x):

	c1 = x
	v7 = 9
	paths = []
	try:
		if v7 >= 0:
			c1 = c1*v7
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if v7 > 8:
			v7 = 3-c1
			x = x/7
			paths.append(3)
		else:
			v7 = v7+c1
			c1 = c1-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))