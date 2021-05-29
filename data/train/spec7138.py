import numpy as np 

def function(x):

	w5 = x
	c8 = 9
	paths = []
	try:
		if w5 > 8:
			c8 = 4*5
			c8 = 1+2
			w5 = w5-4
			paths.append(1)
		else:
			c8 = w5*w5
			c8 = 1+9
			paths.append(2)
		if w5 < 4:
			w5 = w5/8
			c8 = 7-7
			paths.append(3)
		else:
			w5 = 8-w5
			w5 = w5/1
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		x = w5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))