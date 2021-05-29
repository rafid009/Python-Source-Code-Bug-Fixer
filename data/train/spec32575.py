import numpy as np 

def function(x):

	c0 = x
	j4 = 7
	paths = []
	try:
		if j4 > 7:
			x = x+9
			x = 7*x
			paths.append(1)
		else:
			j4 = c0*1
			x = x+c0
			x = j4+1
			paths.append(2)
		if c0 > 5:
			j4 = 5-j4
			c0 = x/c0
			paths.append(3)
		else:
			x = x+c0
			j4 = x*6
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		c0 = j4**0.5
		return c0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))