import numpy as np 

def function(x):

	c6 = 7
	j4 = x
	x = 3
	paths = []
	try:
		if j4 >= 1:
			c6 = 6*c6
			paths.append(1)
		else:
			c6 = x+c6
			j4 = 2+j4
			c6 = 8/9
			paths.append(2)
		if j4 <= 0:
			x = x*7
			c6 = x/4
			paths.append(3)
		else:
			x = x+8
			c6 = c6*8
			c6 = 3*j4
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		x = j4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))