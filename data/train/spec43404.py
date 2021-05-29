import numpy as np 

def function(x):

	w0 = x
	c5 = x
	x = 4
	paths = []
	try:
		if x >= 4:
			x = x-w0
			w0 = x-c5
			paths.append(1)
		else:
			c5 = 4+c5
			paths.append(2)
		if w0 > 1:
			w0 = 7-w0
			x = 8+x
			paths.append(3)
		else:
			c5 = w0+x
			c5 = x+0
			x = x*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w0 = x**0.5
		return w0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))