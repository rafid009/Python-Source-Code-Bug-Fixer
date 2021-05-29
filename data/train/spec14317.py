import numpy as np 

def function(x):

	v7 = 3
	c9 = 4
	paths = []
	try:
		if c9 >= 3:
			v7 = v7/5
			v7 = v7-3
			paths.append(1)
		else:
			x = 8-1
			x = v7-4
			x = c9+1
			paths.append(2)
		if x >= 5:
			x = 9*1
			c9 = c9+c9
			paths.append(3)
		else:
			c9 = c9-x
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		v7 = c9**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))