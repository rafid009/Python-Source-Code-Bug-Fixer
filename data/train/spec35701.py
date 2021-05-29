import numpy as np 

def function(x):

	v5 = x
	c7 = x
	paths = []
	try:
		if v5 >= 0:
			x = 1-x
			paths.append(1)
		else:
			x = x-v5
			v5 = v5*9
			paths.append(2)
		if v5 >= 2:
			c7 = 9-c7
			x = 1+c7
			paths.append(3)
		else:
			x = 4-x
			v5 = c7*9
			x = x+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))