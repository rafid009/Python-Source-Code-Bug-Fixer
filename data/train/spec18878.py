import numpy as np 

def function(x):

	w4 = x
	c3 = 9
	paths = []
	try:
		if x < 1:
			w4 = w4*2
			paths.append(1)
		else:
			x = x*w4
			c3 = c3-0
			x = x+x
			paths.append(2)
		if w4 > 5:
			x = 2-2
			w4 = w4*x
			paths.append(3)
		else:
			c3 = 2+c3
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		c3 = w4**0.5
		return c3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))