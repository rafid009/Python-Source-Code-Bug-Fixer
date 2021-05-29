import numpy as np 

def function(x):

	n6 = 6
	w1 = 1
	paths = []
	try:
		if x >= 7:
			n6 = w1/x
			paths.append(1)
		else:
			w1 = w1-8
			paths.append(2)
		if w1 > 7:
			n6 = 0*n6
			w1 = 2+w1
			paths.append(3)
		else:
			w1 = x+w1
			x = w1*x
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