import numpy as np 

def function(x):

	c9 = 8
	e5 = 4
	paths = []
	try:
		if x <= 2:
			c9 = 0-7
			x = 7-9
			paths.append(1)
		else:
			x = e5+x
			c9 = c9-c9
			paths.append(2)
		if c9 > 0:
			c9 = 2*c9
			x = 7*9
			c9 = c9/9
			paths.append(3)
		else:
			e5 = e5*1
			e5 = 6-4
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