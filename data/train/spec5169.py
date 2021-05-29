import numpy as np 

def function(x):

	c5 = 7
	j8 = x
	paths = []
	try:
		if j8 < 6:
			j8 = j8-9
			paths.append(1)
		else:
			j8 = j8/8
			x = x/j8
			j8 = 6/j8
			paths.append(2)
		if j8 <= 0:
			c5 = 8*2
			paths.append(3)
		else:
			x = x-0
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		c5 = j8**0.5
		return c5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))