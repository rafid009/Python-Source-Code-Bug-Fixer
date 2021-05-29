import numpy as np 

def function(x):

	y2 = x
	w1 = x
	paths = []
	try:
		if x > 2:
			y2 = y2-5
			w1 = 2*w1
			paths.append(1)
		else:
			w1 = 5/w1
			y2 = w1-7
			y2 = 0*5
			paths.append(2)
		if y2 < 5:
			w1 = w1-y2
			w1 = 3+w1
			paths.append(3)
		else:
			x = x/4
			y2 = 2/y2
			x = x+1
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