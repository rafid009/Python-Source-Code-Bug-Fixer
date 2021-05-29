import numpy as np 

def function(x):

	w1 = x
	x0 = 2
	paths = []
	try:
		if x < 1:
			x = 0-w1
			x0 = 8-x0
			x0 = x0/4
			paths.append(1)
		else:
			x0 = x0+5
			x = 3+2
			w1 = 6/2
			paths.append(2)
		if x0 >= 8:
			x = x*x0
			paths.append(3)
		else:
			x = x0-x
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		w1 = w1**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))