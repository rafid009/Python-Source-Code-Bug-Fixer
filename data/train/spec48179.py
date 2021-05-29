import numpy as np 

def function(x):

	c0 = x
	w1 = 2
	paths = []
	try:
		if w1 > 3:
			w1 = w1+6
			paths.append(1)
		else:
			w1 = c0+w1
			x = 2-3
			x = c0-4
			paths.append(2)
		if x <= 7:
			x = 3+3
			w1 = 3/1
			paths.append(3)
		else:
			c0 = c0-9
			c0 = 3*w1
			c0 = 4*w1
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