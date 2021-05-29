import numpy as np 

def function(x):

	j4 = x
	c8 = 5
	paths = []
	try:
		if j4 > 0:
			c8 = c8-8
			j4 = j4*2
			x = 0-6
			paths.append(1)
		else:
			c8 = 6+c8
			x = x-8
			paths.append(2)
		if j4 <= 4:
			j4 = c8/c8
			j4 = 1*7
			paths.append(3)
		else:
			j4 = 4*x
			x = 6*j4
			j4 = j4+5
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		c8 = c8**0.5
		return c8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))