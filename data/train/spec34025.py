import numpy as np 

def function(x):

	c9 = x
	e9 = 2
	paths = []
	try:
		if e9 < 5:
			e9 = 8*1
			e9 = e9/6
			paths.append(1)
		else:
			c9 = 6/c9
			e9 = 8*e9
			x = e9-5
			paths.append(2)
		if e9 > 2:
			c9 = 9*e9
			c9 = c9/4
			paths.append(3)
		else:
			c9 = c9/8
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		x = c9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))