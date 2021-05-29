import numpy as np 

def function(x):

	e1 = 1
	c4 = x
	paths = []
	try:
		if e1 >= 4:
			x = x/5
			c4 = c4*8
			paths.append(1)
		else:
			x = 9*3
			c4 = 7/c4
			e1 = 5+e1
			paths.append(2)
		if e1 < 0:
			x = 5+x
			paths.append(3)
		else:
			e1 = 4+8
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		x = c4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))