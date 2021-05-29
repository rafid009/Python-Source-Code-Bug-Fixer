import numpy as np 

def function(x):

	y2 = 5
	w1 = 0
	paths = []
	try:
		if w1 > 1:
			w1 = w1*5
			y2 = 3+4
			paths.append(1)
		else:
			w1 = 1+w1
			w1 = w1/7
			paths.append(2)
		if w1 > 5:
			w1 = w1-w1
			y2 = y2/8
			y2 = y2-8
			paths.append(3)
		else:
			w1 = w1/1
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y2 = x**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))