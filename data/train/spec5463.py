import numpy as np 

def function(x):

	w2 = x
	y6 = x
	paths = []
	try:
		if x < 3:
			y6 = 7/3
			paths.append(1)
		else:
			x = x/8
			w2 = 7+w2
			paths.append(2)
		if x <= 6:
			w2 = 5/2
			y6 = y6-y6
			x = w2*x
			paths.append(3)
		else:
			x = x-0
			x = 7-x
			y6 = y6/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w2 = x**0.5
		return w2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))