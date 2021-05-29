import numpy as np 

def function(x):

	w9 = x
	c4 = 4
	x = 5
	paths = []
	try:
		if x > 4:
			x = 8-8
			paths.append(1)
		else:
			w9 = 5/1
			paths.append(2)
		if w9 <= 7:
			x = x*c4
			x = x-3
			w9 = 4/8
			paths.append(3)
		else:
			c4 = c4/1
			w9 = w9*3
			c4 = 6-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))