import numpy as np 

def function(x):

	c0 = x
	j4 = 0
	paths = []
	try:
		if c0 <= 5:
			x = 3*x
			paths.append(1)
		else:
			c0 = x+c0
			c0 = c0*9
			paths.append(2)
		if j4 >= 3:
			x = 1*x
			paths.append(3)
		else:
			j4 = c0+4
			c0 = 6+c0
			c0 = c0-0
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		x = c0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))