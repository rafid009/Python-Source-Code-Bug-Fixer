import numpy as np 

def function(x):

	w1 = 2
	d4 = x
	paths = []
	try:
		if x <= 7:
			w1 = 9*7
			d4 = d4*w1
			paths.append(1)
		else:
			d4 = d4/3
			paths.append(2)
		if x < 5:
			d4 = 2*x
			paths.append(3)
		else:
			d4 = 1/x
			d4 = 2+7
			w1 = 7-w1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d4 = x**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))