import numpy as np 

def function(x):

	c6 = 4
	j4 = 7
	paths = []
	try:
		if c6 < 6:
			c6 = c6+9
			c6 = 6-x
			paths.append(1)
		else:
			j4 = j4+6
			j4 = j4-8
			j4 = 0/1
			paths.append(2)
		if x >= 6:
			c6 = c6-6
			paths.append(3)
		else:
			j4 = 7/j4
			j4 = c6*j4
			x = c6-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j4 = x**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))