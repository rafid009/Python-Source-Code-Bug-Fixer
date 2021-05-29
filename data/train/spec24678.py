import numpy as np 

def function(x):

	j1 = x
	c7 = 3
	x = x
	paths = []
	try:
		if c7 <= 2:
			x = j1/7
			x = 4-2
			x = 8-x
			paths.append(1)
		else:
			c7 = x/9
			paths.append(2)
		if c7 <= 1:
			c7 = 2-x
			paths.append(3)
		else:
			j1 = 4/j1
			x = 4-x
			c7 = 8-c7
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		x = j1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))