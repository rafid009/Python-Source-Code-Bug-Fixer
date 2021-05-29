import numpy as np 

def function(x):

	w9 = x
	l4 = 5
	paths = []
	try:
		if x >= 8:
			w9 = 1/2
			x = x/4
			paths.append(1)
		else:
			l4 = w9/x
			l4 = 4/w9
			paths.append(2)
		if w9 >= 9:
			w9 = 3*l4
			paths.append(3)
		else:
			x = x-2
			x = 1*6
			w9 = 8/w9
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		x = l4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))