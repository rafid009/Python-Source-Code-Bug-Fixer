import numpy as np 

def function(x):

	c1 = 3
	j4 = 9
	paths = []
	try:
		if j4 > 8:
			x = 4/x
			c1 = 2+c1
			paths.append(1)
		else:
			c1 = c1-j4
			x = x-x
			paths.append(2)
		if x <= 9:
			x = x/9
			x = x-0
			paths.append(3)
		else:
			x = x+2
			j4 = c1+j4
			j4 = c1/j4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))