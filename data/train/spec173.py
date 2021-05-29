import numpy as np 

def function(x):

	w4 = 1
	c1 = x
	paths = []
	try:
		if x < 4:
			w4 = 2*w4
			x = x/3
			w4 = w4*x
			paths.append(1)
		else:
			c1 = x*c1
			c1 = 5-c1
			paths.append(2)
		if x < 3:
			c1 = 3+c1
			x = 7/7
			paths.append(3)
		else:
			c1 = x*4
			w4 = w4-7
			x = c1/x
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))