import numpy as np 

def function(x):

	w8 = x
	q9 = x
	paths = []
	try:
		if q9 >= 9:
			x = 5*2
			x = 3+x
			x = w8+9
			paths.append(1)
		else:
			x = 7-w8
			paths.append(2)
		if x < 9:
			x = x-5
			w8 = 1/x
			w8 = w8/x
			paths.append(3)
		else:
			q9 = 6*q9
			w8 = 4+x
			x = 2-9
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