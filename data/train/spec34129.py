import numpy as np 

def function(x):

	d2 = 3
	w1 = x
	paths = []
	try:
		if d2 < 9:
			w1 = w1+w1
			w1 = d2-w1
			x = x*5
			paths.append(1)
		else:
			d2 = d2*7
			paths.append(2)
		if x < 6:
			w1 = w1+d2
			paths.append(3)
		else:
			w1 = 2-w1
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