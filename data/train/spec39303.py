import numpy as np 

def function(x):

	w1 = x
	c8 = 0
	x = x
	paths = []
	try:
		if c8 < 5:
			c8 = c8/9
			paths.append(1)
		else:
			x = 9*x
			c8 = c8/c8
			c8 = c8+2
			paths.append(2)
		if w1 <= 9:
			c8 = 5*c8
			c8 = c8/x
			w1 = w1*6
			paths.append(3)
		else:
			w1 = w1*3
			c8 = 8-w1
			w1 = w1/3
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		x = w1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))