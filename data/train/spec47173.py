import numpy as np 

def function(x):

	r9 = 1
	w1 = 3
	paths = []
	try:
		if x > 3:
			x = x*w1
			x = x+6
			paths.append(1)
		else:
			w1 = w1/x
			paths.append(2)
		if r9 >= 0:
			w1 = 3*w1
			r9 = w1-r9
			r9 = 9/1
			paths.append(3)
		else:
			w1 = 2-w1
			x = x/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))