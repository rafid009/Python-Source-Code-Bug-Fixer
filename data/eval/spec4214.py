import numpy as np 

def function(x):

	c1 = 3
	j1 = 2
	paths = []
	try:
		if j1 > 0:
			c1 = 9-c1
			j1 = c1/3
			paths.append(1)
		else:
			c1 = 5+c1
			paths.append(2)
		if x >= 7:
			j1 = 6/j1
			x = x+j1
			paths.append(3)
		else:
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j1 = x**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))