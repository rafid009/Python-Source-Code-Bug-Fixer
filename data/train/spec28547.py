import numpy as np 

def function(x):

	c4 = 3
	v7 = x
	x = x
	paths = []
	try:
		if v7 >= 2:
			v7 = x/4
			v7 = v7/x
			paths.append(1)
		else:
			v7 = 6-5
			c4 = c4+v7
			c4 = c4*v7
			paths.append(2)
		if v7 > 2:
			x = c4/8
			v7 = 8-v7
			c4 = c4/4
			paths.append(3)
		else:
			c4 = x-5
			x = c4/4
			c4 = 7/c4
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		v7 = c4**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))