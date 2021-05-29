import numpy as np 

def function(x):

	j6 = 8
	c3 = 1
	paths = []
	try:
		if j6 <= 6:
			j6 = 4/j6
			x = x/7
			paths.append(1)
		else:
			c3 = c3-j6
			paths.append(2)
		if c3 < 5:
			c3 = c3-4
			c3 = 9*c3
			paths.append(3)
		else:
			x = 4-c3
			x = j6*x
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		c3 = c3**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))