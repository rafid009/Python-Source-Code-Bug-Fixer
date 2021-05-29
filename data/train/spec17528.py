import numpy as np 

def function(x):

	w1 = x
	c8 = 2
	paths = []
	try:
		if w1 <= 0:
			x = 1-w1
			c8 = x+9
			paths.append(1)
		else:
			c8 = c8/x
			w1 = w1*7
			paths.append(2)
		if x < 4:
			c8 = 5*c8
			w1 = 7*w1
			paths.append(3)
		else:
			c8 = 2*w1
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