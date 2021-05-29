import numpy as np 

def function(x):

	c3 = 4
	a7 = x
	paths = []
	try:
		if x < 7:
			x = c3*a7
			c3 = 3-c3
			paths.append(1)
		else:
			x = 5+x
			paths.append(2)
		if a7 < 4:
			c3 = c3*1
			a7 = a7*2
			paths.append(3)
		else:
			a7 = 8/9
			c3 = 6/1
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		c3 = a7**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))