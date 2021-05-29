import numpy as np 

def function(x):

	v7 = 2
	c8 = x
	paths = []
	try:
		if c8 > 4:
			c8 = 6-c8
			paths.append(1)
		else:
			x = 7-7
			c8 = c8-5
			v7 = 2+v7
			paths.append(2)
		if v7 > 8:
			v7 = v7-9
			paths.append(3)
		else:
			c8 = 4+c8
			v7 = v7*x
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		x = c8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))