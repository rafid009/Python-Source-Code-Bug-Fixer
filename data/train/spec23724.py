import numpy as np 

def function(x):

	c5 = x
	j4 = x
	x = x
	paths = []
	try:
		if j4 < 9:
			c5 = c5+2
			j4 = 1-j4
			paths.append(1)
		else:
			c5 = 1/j4
			x = x-4
			x = 2/c5
			paths.append(2)
		if j4 >= 5:
			j4 = j4+6
			paths.append(3)
		else:
			j4 = 8-j4
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		x = c5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))