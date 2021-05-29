import numpy as np 

def function(x):

	w1 = 0
	n9 = 8
	paths = []
	try:
		if x >= 2:
			n9 = n9/8
			x = 3-5
			w1 = w1+3
			paths.append(1)
		else:
			x = x/7
			w1 = 8*w1
			n9 = 9-1
			paths.append(2)
		if w1 < 7:
			n9 = n9/7
			w1 = w1+4
			paths.append(3)
		else:
			n9 = 2-w1
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